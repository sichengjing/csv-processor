import pytest

from csvlib.reader import get_headers, load


@pytest.fixture
def sample_csv(tmp_path):
    """Create a temporary CSV file for testing."""
    content = "name,age,city\nAlice,30,NYC\nBob,25,LA\nCarol,35,Chicago\n"
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(content, encoding="utf-8")
    return str(csv_file)


def test_load_returns_list(sample_csv):
    data = load(sample_csv)
    assert isinstance(data, list)


def test_load_correct_row_count(sample_csv):
    data = load(sample_csv)
    assert len(data) == 3


def test_load_correct_keys(sample_csv):
    data = load(sample_csv)
    assert set(data[0].keys()) == {"name", "age", "city"}


def test_load_correct_values(sample_csv):
    data = load(sample_csv)
    assert data[0]["name"] == "Alice"
    assert data[1]["age"] == "25"


def test_load_file_not_found():
    with pytest.raises(FileNotFoundError):
        load("nonexistent.csv")


def test_load_wrong_extension(tmp_path):
    txt_file = tmp_path / "data.txt"
    txt_file.write_text("name,age\nAlice,30\n")
    with pytest.raises(ValueError):
        load(str(txt_file))


def test_get_headers(sample_csv):
    data = load(sample_csv)
    headers = get_headers(data)
    assert headers == ["name", "age", "city"]


def test_get_headers_empty():
    assert get_headers([]) == []
