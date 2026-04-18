import pytest

from csvlib.filter import filter_rows


@pytest.fixture
def sample_data():
    return [
        {"name": "Alice", "age": "30", "city": "NYC"},
        {"name": "Bob", "age": "25", "city": "LA"},
        {"name": "Carol", "age": "35", "city": "NYC"},
        {"name": "Dave", "age": "25", "city": "Chicago"},
    ]


def test_filter_equal_numeric(sample_data):
    result = filter_rows(sample_data, "age", "=", "25")
    assert len(result) == 2
    assert all(r["age"] == "25" for r in result)


def test_filter_equal_string(sample_data):
    result = filter_rows(sample_data, "city", "=", "NYC")
    assert len(result) == 2
    assert all(r["city"] == "NYC" for r in result)


def test_filter_not_equal(sample_data):
    result = filter_rows(sample_data, "city", "!=", "NYC")
    assert len(result) == 2
    assert all(r["city"] != "NYC" for r in result)


def test_filter_greater_than(sample_data):
    result = filter_rows(sample_data, "age", ">", "28")
    assert len(result) == 2
    assert all(float(r["age"]) > 28 for r in result)


def test_filter_greater_equal(sample_data):
    result = filter_rows(sample_data, "age", ">=", "30")
    assert len(result) == 2


def test_filter_less_than(sample_data):
    result = filter_rows(sample_data, "age", "<", "30")
    assert len(result) == 2
    assert all(float(r["age"]) < 30 for r in result)


def test_filter_less_equal(sample_data):
    result = filter_rows(sample_data, "age", "<=", "30")
    assert len(result) == 3


def test_filter_no_match(sample_data):
    result = filter_rows(sample_data, "age", ">", "100")
    assert result == []


def test_filter_invalid_operator(sample_data):
    with pytest.raises(ValueError):
        filter_rows(sample_data, "age", "??", "30")


def test_filter_invalid_column(sample_data):
    with pytest.raises(KeyError):
        filter_rows(sample_data, "salary", "=", "1000")


def test_filter_empty_data():
    assert filter_rows([], "age", ">", "30") == []