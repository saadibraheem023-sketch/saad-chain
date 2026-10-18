import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = BASE_DIR / "documents"


def analyze_csv(filename: str) -> str:
    """
    Analyze a CSV file and return a summary.
    """

    file_path = DOCUMENTS_DIR / filename

    if not file_path.exists():
        return f"File not found: {filename}"

    try:

        df = pd.read_csv(file_path)

        result = []

        result.append(f"Rows: {len(df)}")
        result.append(f"Columns: {len(df.columns)}")

        result.append(
            "Columns: " +
            ", ".join(df.columns.astype(str))
        )

        result.append("\nData types:")

        result.append(
            df.dtypes.to_string()
        )

        result.append("\nMissing values:")

        result.append(
            df.isnull().sum().to_string()
        )

        result.append("\nNumeric summary:")

        result.append(
            df.describe().to_string()
        )

        return "\n".join(result)

    except Exception as e:

        return f"CSV analysis error: {e}"