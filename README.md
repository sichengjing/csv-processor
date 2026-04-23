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
- **How it was used**: Used to generate initial code for each module, write tests, debug errors, and provide guidance on project structure and Git workflow.
- **What it produced**: Drafts of all Python modules (`reader.py`, `filter.py`, `sorter.py`, `aggregator.py`, `exporter.py`, `cli/main.py`), test files, `pyproject.toml`, `ci.yml`, and this README.
- **Review process**: All generated code was reviewed, tested locally, and modified where necessary before committing.