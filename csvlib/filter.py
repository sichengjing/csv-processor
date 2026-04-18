def filter_rows(data: list[dict], column: str, op: str, value: str) -> list[dict]:
    """
    Filter rows based on a condition applied to a column.

    Supports both numeric and string comparisons. If the column
    values can be converted to float, numeric comparison is used;
    otherwise, string comparison is used.

    Args:
        data: List of dicts returned by load().
        column: Column name to filter on.
        op: Comparison operator, one of: '=', '!=', '>', '>=', '<', '<='.
        value: Value to compare against (as a string).

    Returns:
        A filtered list of dicts.

    Raises:
        KeyError: If the column does not exist in the data.
        ValueError: If the operator is not supported.
    """
    supported_ops = {"=", "!=", ">", ">=", "<", "<="}

    if op not in supported_ops:
        raise ValueError(f"Unsupported operator '{op}'. Choose from: {supported_ops}")

    if data and column not in data[0]:
        available = list(data[0].keys())
        raise KeyError(f"Column '{column}' not found. Available: {available}")

    def matches(row: dict) -> bool:
        cell = row[column]

        try:
            cell_val = float(cell)
            cmp_val = float(value)
            numeric = True
        except ValueError:
            cell_val = cell
            cmp_val = value
            numeric = False

        if op == "=":
            return cell_val == cmp_val
        elif op == "!=":
            return cell_val != cmp_val
        elif op == ">":
            return numeric and cell_val > cmp_val
        elif op == ">=":
            return numeric and cell_val >= cmp_val
        elif op == "<":
            return numeric and cell_val < cmp_val
        elif op == "<=":
            return numeric and cell_val <= cmp_val

    return [row for row in data if matches(row)]