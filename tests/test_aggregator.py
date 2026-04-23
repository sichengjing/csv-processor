import pytest

from csvlib.aggregator import col_count, col_max, col_mean, col_min, col_sum


@pytest.fixture
def sample_data():
    return [
        {"name": "Alice", "age": "30", "score": "85.5"},
        {"name": "Bob", "age": "25", "score": "90.0"},
        {"name": "Carol", "age": "35", "score": "78.5"},
        {"name": "Dave", "age": "25", "score": "92.0"},
    ]


def test_sum(sample_data):
    assert col_sum(sample_data, "age") == 115.0


def test_mean(sample_data):
    assert col_mean(sample_data, "age") == 28.75


def test_min(sample_data):
    assert col_min(sample_data, "age") == 25.0


def test_max(sample_data):
    assert col_max(sample_data, "age") == 35.0


def test_count(sample_data):
    assert col_count(sample_data, "name") == 4


def test_sum_float(sample_data):
    assert col_sum(sample_data, "score") == 346.0


def test_mean_float(sample_data):
    assert col_mean(sample_data, "score") == 86.5


def test_invalid_column(sample_data):
    with pytest.raises(KeyError):
        col_sum(sample_data, "salary")


def test_non_numeric_column(sample_data):
    with pytest.raises(ValueError):
        col_sum(sample_data, "name")


def test_empty_data():
    assert col_sum([], "age") == 0.0


def test_count_empty_data():
    assert col_count([], "age") == 0
