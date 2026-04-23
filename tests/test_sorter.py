import pytest

from csvlib.sorter import sort_by


@pytest.fixture
def sample_data():
    return [
        {"name": "Carol", "age": "35", "city": "NYC"},
        {"name": "Alice", "age": "30", "city": "LA"},
        {"name": "Bob", "age": "25", "city": "Chicago"},
        {"name": "Dave", "age": "25", "city": "NYC"},
    ]


def test_sort_numeric_ascending(sample_data):
    result = sort_by(sample_data, "age")
    ages = [float(r["age"]) for r in result]
    assert ages == sorted(ages)


def test_sort_numeric_descending(sample_data):
    result = sort_by(sample_data, "age", reverse=True)
    ages = [float(r["age"]) for r in result]
    assert ages == sorted(ages, reverse=True)


def test_sort_string_ascending(sample_data):
    result = sort_by(sample_data, "name")
    names = [r["name"] for r in result]
    assert names == sorted(names)


def test_sort_string_descending(sample_data):
    result = sort_by(sample_data, "name", reverse=True)
    names = [r["name"] for r in result]
    assert names == sorted(names, reverse=True)


def test_sort_does_not_modify_original(sample_data):
    original = [r.copy() for r in sample_data]
    sort_by(sample_data, "age")
    assert sample_data == original


def test_sort_invalid_column(sample_data):
    with pytest.raises(KeyError):
        sort_by(sample_data, "salary")


def test_sort_empty_data():
    assert sort_by([], "age") == []
