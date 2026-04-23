import json

import pytest

from csvlib.exporter import save, to_csv, to_json, to_tsv


@pytest.fixture
def sample_data():
    return [
        {"name": "Alice", "age": "30", "city": "NYC"},
        {"name": "Bob", "age": "25", "city": "LA"},
    ]


def test_to_json_is_valid(sample_data):
    result = to_json(sample_data)
    parsed = json.loads(result)
    assert parsed == sample_data


def test_to_json_correct_length(sample_data):
    result = to_json(sample_data)
    parsed = json.loads(result)
    assert len(parsed) == 2


def test_to_json_indent(sample_data):
    result = to_json(sample_data, indent=4)
    assert "    " in result


def test_to_tsv_has_tabs(sample_data):
    result = to_tsv(sample_data)
    assert "\t" in result


def test_to_tsv_correct_rows(sample_data):
    result = to_tsv(sample_data)
    lines = result.strip().split("\n")
    assert len(lines) == 3


def test_to_tsv_header(sample_data):
    result = to_tsv(sample_data)
    first_line = result.split("\n")[0].strip()
    assert "name\tage\tcity" == first_line


def test_to_csv_correct_rows(sample_data):
    result = to_csv(sample_data)
    lines = result.strip().split("\n")
    assert len(lines) == 3


def test_to_csv_header(sample_data):
    result = to_csv(sample_data)
    first_line = result.split("\n")[0]
    assert "name" in first_line
    assert "age" in first_line


def test_to_json_empty():
    assert to_json([]) == "[]"


def test_to_tsv_empty():
    assert to_tsv([]) == ""


def test_to_csv_empty():
    assert to_csv([]) == ""


def test_save(tmp_path, sample_data):
    content = to_json(sample_data)
    filepath = str(tmp_path / "output.json")
    save(content, filepath)
    with open(filepath, encoding="utf-8") as f:
        saved = f.read()
    assert saved == content
