# CSV Processor

A lightweight Python library for processing CSV files, with a command-line interface.

## Architecture

The project is split into two layers:

- **`csvlib/`** — core library (business logic)
  - `reader.py` — load CSV files
  - `filter.py` — filter rows by condition
  - `sorter.py` — sort rows by column
  - `aggregator.py` — compute statistics
  - `exporter.py` — export to JSON, TSV, or CSV
- **`cli/`** — command-line interface (calls the library)

## Installation

Requires Python 3.11+.

```bash
git clone https://github.com/sichengjing/csv-processor.git
cd csv-processor
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Running Tests

```bash
pip install pytest ruff
pytest tests/ -v
```

## Code Style

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting.

```bash
ruff check .
ruff format .
```

## CLI Usage

### Show column headers

```bash
python -m cli.main headers data.csv
```

### Filter rows

```bash
python -m cli.main filter data.csv --column age --op ">" --value 30
```

Supported operators: `=`, `!=`, `>`, `>=`, `<`, `<=`

### Sort rows

```bash
# Ascending
python -m cli.main sort data.csv --column age

# Descending
python -m cli.main sort data.csv --column age --desc
```

### Show statistics

```bash
python -m cli.main stats data.csv --column age
```

### Export to another format

```bash
# Print to terminal
python -m cli.main export data.csv --format json
python -m cli.main export data.csv --format tsv

# Save to file
python -m cli.main export data.csv --format json --output output.json
```

## Library Usage

```python
from csvlib.reader import load, get_headers
from csvlib.filter import filter_rows
from csvlib.sorter import sort_by
from csvlib.aggregator import col_mean, col_sum
from csvlib.exporter import to_json

# Load data
data = load("data.csv")

# Get headers
headers = get_headers(data)

# Filter
adults = filter_rows(data, "age", ">", "18")

# Sort
sorted_data = sort_by(data, "age")

# Statistics
mean_age = col_mean(data, "age")

# Export
json_str = to_json(data)
```

## AI Tools Usage

This project was developed with assistance from Claude (Anthropic).

- **Tool used**: Claude (claude.ai)
- **How it was used**: Used to assist with code drafting, debugging, and getting suggestions on project structure and Git workflow.
- **What it produced**: Helped generate initial drafts for some Python modules, test files, and configuration files.
- **Review process**: All generated code was reviewed, tested locally, and modified where necessary before committing.

## Group Members
- Sicheng Jing (solo project)
