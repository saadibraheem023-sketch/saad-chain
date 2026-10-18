from pathlib import Path
import os
from datetime import datetime
# داخل ملف tools.py
import datetime



BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = BASE_DIR / "documents"


def get_current_time() -> str:
    """
    Get the current local date and time.

    Returns:
        str: Current date and time.
    """

    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate(expression: str) -> str:
    """
    Calculate a mathematical expression.

    Args:
        expression: Mathematical expression such as 25 * 4.

    Returns:
        str: Calculation result.
    """

    allowed = "0123456789+-*/().% "

    if not all(char in allowed for char in expression):
        return "Expression contains unsupported characters."

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"


def list_documents() -> str:
    """
    List files inside the documents folder.

    Returns:
        str: List of available documents.
    """

    DOCUMENTS_DIR.mkdir(exist_ok=True)

    files = []

    for file in DOCUMENTS_DIR.iterdir():

        if file.is_file():
            files.append(file.name)

    if not files:
        return "No documents found."

    return "\n".join(files)


def read_document(filename: str) -> str:
    """
    Read a text document from the documents folder.

    Args:
        filename: Name of the document.

    Returns:
        str: Document contents.
    """

    file_path = DOCUMENTS_DIR / filename

    if not file_path.exists():
        return f"File not found: {filename}"

    if not file_path.is_file():
        return "This is not a file."

    try:

        return file_path.read_text(encoding="utf-8")

    except Exception as e:

        return f"Could not read file: {e}"

    TOOLS = [
        get_current_time,
        calculate,
        list_documents,
        read_document,
        create_document,
]


def create_document(filename: str, content: str) -> str:
    """
    Create a text document inside the documents folder.

    Args:
        filename: Name of the new document.
        content: Content of the document.

    Returns:
        str: Operation result.
    """

    DOCUMENTS_DIR.mkdir(exist_ok=True)

    file_path = DOCUMENTS_DIR / filename

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    return f"Document created successfully: {filename}"