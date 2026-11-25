from flask import Flask, render_template, request
from checker import check_pep8

app = Flask(__name__)

MAX_CODE_LENGTH = 50_000


@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    errors = []
    checked = False
    empty_input = False

    if request.method == "POST":
        checked = True
        code = request.form.get("code", "")

        if not code.strip():
            empty_input = True
        elif len(code) > MAX_CODE_LENGTH:
            errors = [{
                "line": 1,
                "column": 1,
                "code": "LIMIT",
                "message": (
                    f"Kod przekracza limit {MAX_CODE_LENGTH} znaków."
                ),
                "why": (
                    "Zbyt duży fragment tekstu może spowolnić "
                    "sprawdzanie na serwerze."
                ),
                "fix": (
                    "Wklej krótszy fragment kodu "
                ),
                "doc_url": "https://peps.python.org/pep-0008/",
            }]
        else:
            errors = check_pep8(code)

    error_count = sum(1 for err in errors if err.get("severity") != "warning")
    warning_count = sum(1 for err in errors if err.get("severity") == "warning")

    return render_template(
        "index.html",
        code=code,
        errors=errors,
        checked=checked,
        empty_input=empty_input,
        error_count=error_count,
        warning_count=warning_count,
    )


if __name__ == "__main__":
    app.run(debug=True)
