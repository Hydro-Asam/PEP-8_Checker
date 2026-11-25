import pycodestyle

from pep8_advice import DEFAULT_ADVICE, PEP8_ADVICE


def _get_severity(code: str) -> str:
    """Zwraca 'warning' dla kodów W..., a dla reszty 'error'."""
    if code.startswith("W"):
        return "warning"
    return "error"

def _get_doc_url(code: str) -> str:
    """Buduje link do strony Flake8 Rules dla kodów błędów i ostrzeżeń."""
    if code.startswith(("E", "W")) and len(code) == 4 and code[1:].isdigit():
        return f"https://www.flake8rules.com/rules/{code}.html"
    return "https://www.flake8rules.com/"

class ListReport(pycodestyle.BaseReport):
    """Własny raport, który zamiast wypisywać na ekran, zbiera błędy do listy."""

    def __init__(self, options):
        super().__init__(options)
        self.errors = []

    def error(self, line_number, offset, text, check):
        code = super().error(line_number, offset, text, check)
        if code:
            advice = PEP8_ADVICE.get(code, DEFAULT_ADVICE)
            self.errors.append({
                "line": line_number,
                "column": offset + 1,
                "code": code,
                "severity": _get_severity(code),
                "message": text,
                "why": advice["why"],
                "fix": advice["fix"],
                "doc_url": _get_doc_url(code),
            })
        return code


def check_pep8(source_code: str) -> list[dict]:
    """Sprawdza przekazany kod źródłowy pod kątem zgodności z PEP 8."""
    style_guide = pycodestyle.StyleGuide(reporter=ListReport)
    lines = source_code.splitlines(keepends=True)

    checker = pycodestyle.Checker(
        filename="<input>",
        lines=lines,
        options=style_guide.options,
        report=style_guide.options.report,
    )
    checker.check_all()
    return checker.report.errors


if __name__ == "__main__":
    sample_code = """def badFunction( x,y ):
      z=x+y
      return z
"""
    results = check_pep8(sample_code)
    for err in results:
        level = "OSTRZEŻENIE" if err["severity"] == "warning" else "BŁĄD"
        print(
            f"[{level}] Linia {err['line']}, kol. {err['column']} "
            f"[{err['code']}]: {err['message']}"
        )
        print(f"   Czemu: {err['why']}")
        print(f"   Jak poprawić: {err['fix']}")


