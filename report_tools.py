from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "reports"


def create_pdf_report(
    filename: str,
    title: str,
    content: str
) -> str:

    REPORTS_DIR.mkdir(exist_ok=True)

    file_path = REPORTS_DIR / filename

    styles = getSampleStyleSheet()

    document = SimpleDocTemplate(
        str(file_path)
    )

    story = []

    story.append(
        Paragraph(
            title,
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    for line in content.split("\n"):

        story.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

        story.append(
            Spacer(1, 8)
        )

    document.build(story)

    return f"PDF created: {file_path}"