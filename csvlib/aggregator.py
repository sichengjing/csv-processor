def _get_numeric_values(data: list[dict], column: str) -> list[float]:
    """
    Extract numeric values from a column.

    Raises:
        KeyError: If the column does not exist.
        ValueError: If no numeric values are found in the column.
    """
    if not data:
        return []

    if column not in data[0]:
        available = list(data[0].keys())
        raise KeyError(f"Column '{column}' not found. Available: {available}")

    values = []
    for row in data:
        try:
            values.append(float(row[column]))
        except ValueError:
            continue

    if not values:
        raise ValueError(f"No numeric values found in column '{column}'.")

    return values


def col_sum(data: list[dict], column: str) -> float:
    """
    Return the sum of numeric values in a column.

    Args:
        data: List of dicts returned by load().
        column: Column name to aggregate.

    Returns:
        Sum as a float.
    """
    return sum(_get_numeric_values(data, column))


def col_mean(data: list[dict], column: str) -> float:
    """
    Return the mean of numeric values in a column.

    Args:
        data: List of dicts returned by load().
        column: Column name to aggregate.

    Returns:
        Mean as a float.
    """
    values = _get_numeric_values(data, column)
    return sum(values) / len(values)


def col_min(data: list[dict], column: str) -> float:
    """
    Return the minimum of numeric values in a column.

    Args:
        data: List of dicts returned by load().
        column: Column name to aggregate.

    Returns:
        Minimum as a float.
    """
    return min(_get_numeric_values(data, column))


def col_max(data: list[dict], column: str) -> float:
    """
    Return the maximum of numeric values in a column.

    Args:
        data: List of dicts returned by load().
        column: Column name to aggregate.

    Returns:
        Maximum as a float.
    """
    return max(_get_numeric_values(data, column))


def col_count(data: list[dict], column: str) -> int:
    """
    Return the count of non-empty values in a column.

    Args:
        data: List of dicts returned by load().
        column: Column name to count.

    Returns:
        Count as an integer.
    """
    if not data:
        return 0

    if column not in data[0]:
        available = list(data[0].keys())
        raise KeyError(f"Column '{column}' not found. Available: {available}")

    return sum(1 for row in data if row[column].strip() != "")
