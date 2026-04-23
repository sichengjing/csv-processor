def sort_by(data: list[dict], column: str, reverse: bool = False) -> list[dict]:
    """
    Sort rows by a given column.

    If the column values can be converted to float, numeric sorting
    is used; otherwise, string sorting is used.

    Args:
        data: List of dicts returned by load().
        column: Column name to sort by.
        reverse: If True, sort in descending order. Default is ascending.

    Returns:
        A new sorted list of dicts.

    Raises:
        KeyError: If the column does not exist in the data.
    """
    if not data:
        return []

    if column not in data[0]:
        available = list(data[0].keys())
        raise KeyError(f"Column '{column}' not found. Available: {available}")

    def sort_key(row: dict):
        val = row[column]
        try:
            return (0, float(val))
        except ValueError:
            return (1, val)

    return sorted(data, key=sort_key, reverse=reverse)
