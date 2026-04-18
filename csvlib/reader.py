import csv
from pathlib import Path


def load(filepath: str) -> list[dict]:
    """
    Load a CSV file and return a list of rows as dictionaries.

    Each row is represented as a dict where keys are column headers.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A list of dicts, one per row.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a valid CSV.
    """
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    if path.suffix.lower() != ".csv":
        raise ValueError(f"File must be a .csv file, got: {path.suffix}")

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    return rows


def get_headers(data: list[dict]) -> list[str]:
    """
    Return the column headers from loaded CSV data.

    Args:
        data: List of dicts returned by load().

    Returns:
        A list of column header strings.
    """
    if not data:
        return []
    return list(data[0].keys())