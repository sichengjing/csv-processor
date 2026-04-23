import csv
import json
from io import StringIO


def to_json(data: list[dict], indent: int = 2) -> str:
    """
    Convert CSV data to a JSON string.

    Args:
        data: List of dicts returned by load().
        indent: Number of spaces for indentation. Default is 2.

    Returns:
        A formatted JSON string.
    """
    return json.dumps(data, indent=indent)


def to_tsv(data: list[dict]) -> str:
    """
    Convert CSV data to a TSV (tab-separated values) string.

    Args:
        data: List of dicts returned by load().

    Returns:
        A TSV formatted string.
    """
    if not data:
        return ""

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys(), delimiter="\t")
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def to_csv(data: list[dict]) -> str:
    """
    Convert CSV data back to a CSV string.

    Args:
        data: List of dicts returned by load().

    Returns:
        A CSV formatted string.
    """
    if not data:
        return ""

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def save(content: str, filepath: str) -> None:
    """
    Save a string to a file.

    Args:
        content: String content to write.
        filepath: Path to the output file.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
