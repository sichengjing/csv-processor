import argparse
import sys

from csvlib.aggregator import col_count, col_max, col_mean, col_min, col_sum
from csvlib.exporter import save, to_csv, to_json, to_tsv
from csvlib.filter import filter_rows
from csvlib.reader import get_headers, load
from csvlib.sorter import sort_by


def cmd_headers(args: argparse.Namespace) -> None:
    """Print column headers of a CSV file."""
    data = load(args.file)
    headers = get_headers(data)
    print(", ".join(headers))


def cmd_filter(args: argparse.Namespace) -> None:
    """Filter rows and print results."""
    data = load(args.file)
    result = filter_rows(data, args.column, args.op, args.value)
    _print_data(result)


def cmd_sort(args: argparse.Namespace) -> None:
    """Sort rows and print results."""
    data = load(args.file)
    result = sort_by(data, args.column, reverse=args.desc)
    _print_data(result)


def cmd_stats(args: argparse.Namespace) -> None:
    """Print summary statistics for a column."""
    data = load(args.file)
    print(f"count : {col_count(data, args.column)}")
    print(f"sum   : {col_sum(data, args.column)}")
    print(f"mean  : {col_mean(data, args.column):.4f}")
    print(f"min   : {col_min(data, args.column)}")
    print(f"max   : {col_max(data, args.column)}")


def cmd_export(args: argparse.Namespace) -> None:
    """Export CSV data to another format."""
    data = load(args.file)

    fmt = args.format.lower()
    if fmt == "json":
        content = to_json(data)
    elif fmt == "tsv":
        content = to_tsv(data)
    elif fmt == "csv":
        content = to_csv(data)
    else:
        print(f"Unsupported format: {fmt}. Choose from: json, tsv, csv.")
        sys.exit(1)

    if args.output:
        save(content, args.output)
        print(f"Saved to {args.output}")
    else:
        print(content)


def _print_data(data: list[dict]) -> None:
    """Print list of dicts as a simple table."""
    if not data:
        print("No results.")
        return

    headers = list(data[0].keys())
    print(", ".join(headers))
    print("-" * 40)
    for row in data:
        print(", ".join(row[h] for h in headers))


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="csvtool",
        description="A simple CSV processing tool.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # headers
    p_headers = subparsers.add_parser("headers", help="Show column headers.")
    p_headers.add_argument("file", help="Path to CSV file.")
    p_headers.set_defaults(func=cmd_headers)

    # filter
    p_filter = subparsers.add_parser("filter", help="Filter rows by condition.")
    p_filter.add_argument("file", help="Path to CSV file.")
    p_filter.add_argument("--column", required=True, help="Column to filter on.")
    p_filter.add_argument(
        "--op",
        required=True,
        choices=["=", "!=", ">", ">=", "<", "<="],
        help="Comparison operator.",
    )
    p_filter.add_argument("--value", required=True, help="Value to compare against.")
    p_filter.set_defaults(func=cmd_filter)

    # sort
    p_sort = subparsers.add_parser("sort", help="Sort rows by a column.")
    p_sort.add_argument("file", help="Path to CSV file.")
    p_sort.add_argument("--column", required=True, help="Column to sort by.")
    p_sort.add_argument("--desc", action="store_true", help="Sort descending.")
    p_sort.set_defaults(func=cmd_sort)

    # stats
    p_stats = subparsers.add_parser("stats", help="Show statistics for a column.")
    p_stats.add_argument("file", help="Path to CSV file.")
    p_stats.add_argument("--column", required=True, help="Column to aggregate.")
    p_stats.set_defaults(func=cmd_stats)

    # export
    p_export = subparsers.add_parser("export", help="Export to another format.")
    p_export.add_argument("file", help="Path to CSV file.")
    p_export.add_argument(
        "--format",
        required=True,
        choices=["json", "tsv", "csv"],
        help="Output format.",
    )
    p_export.add_argument("--output", help="Output file path (optional).")
    p_export.set_defaults(func=cmd_export)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
