from lines import lines_of_code
import pytest
import sys


def test_invalid_py_file(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "file"])
    with pytest.raises(SystemExit):
        lines_of_code()


def test_max_arguments(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "test.py", "extra"])
    with pytest.raises(SystemExit):
        lines_of_code()


def test_min_arguments(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py"])
    with pytest.raises(SystemExit):
        lines_of_code()


def test_unexistent_file(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "unexistent.py"])
    with pytest.raises(SystemExit):
        lines_of_code()


def test_count(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "test.py"])
    assert lines_of_code() == 5


def test_removing_comments(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["lines.py", "test.py"])
    assert lines_of_code()
