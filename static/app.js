const textarea = document.getElementById("codeArea");
const lineNumbers = document.getElementById("lineNumbers");
const cursorPos = document.getElementById("cursorPos");
const lineCount = document.getElementById("lineCount");
const charCount = document.getElementById("charCount");
const clearBtn = document.getElementById("clearBtn");
const resultsContainer = document.getElementById("resultsContainer");

const maxChars = textarea ? (parseInt(textarea.dataset.maxLength, 10) || 50000) : 50000;

function updateCharCount() {
    if (!textarea || !charCount) {
        return;
    }

    const currentLength = textarea.value.length;
    charCount.textContent = "Znaków: " + currentLength + " / " + maxChars;
}

function updateLineNumbers() {
    if (!textarea || !lineNumbers || !lineCount) {
        return;
    }

    const lines = textarea.value.split("\n");
    const total = lines.length;
    let numbersHtml = "";

    for (let i = 1; i <= total; i++) {
        numbersHtml += i + (i < total ? "\n" : "");
    }

    lineNumbers.textContent = numbersHtml;
    lineCount.textContent = "Liczba linii: " + total;
    lineNumbers.scrollTop = textarea.scrollTop;
}

function updateCursorPosition() {
    if (!textarea || !cursorPos) {
        return;
    }

    const pos = textarea.selectionStart || 0;
    const textBefore = textarea.value.slice(0, pos);
    const lines = textBefore.split("\n");
    const line = lines.length;
    const column = lines[lines.length - 1].length + 1;

    cursorPos.textContent = "Linia: " + line + ", Kolumna: " + column;
}

function jumpTo(line, column) {
    if (!textarea) {
        return;
    }

    const lines = textarea.value.split("\n");
    const targetLine = Math.max(1, Math.min(line, lines.length));
    let index = 0;

    for (let i = 0; i < targetLine - 1; i++) {
        index += lines[i].length + 1;
    }

    const targetCol = Math.max(1, column);
    index += Math.min(targetCol - 1, lines[targetLine - 1].length);

    textarea.focus();
    textarea.setSelectionRange(index, index);
    updateCursorPosition();
}

function clearEditor() {
    if (!textarea) {
        return;
    }

    textarea.value = "";
    textarea.focus();
    updateLineNumbers();
    updateCursorPosition();
    updateCharCount();

    if (resultsContainer) {
        resultsContainer.innerHTML = "";
    }
}

if (textarea) {
    textarea.addEventListener("input", () => {
        updateLineNumbers();
        updateCursorPosition();
        updateCharCount();
    });

    textarea.addEventListener("click", updateCursorPosition);
    textarea.addEventListener("keyup", updateCursorPosition);
    textarea.addEventListener("scroll", () => {
        if (lineNumbers) {
            lineNumbers.scrollTop = textarea.scrollTop;
        }
    });
}

if (clearBtn) {
    clearBtn.addEventListener("click", clearEditor);
}

updateLineNumbers();
updateCursorPosition();
updateCharCount();
