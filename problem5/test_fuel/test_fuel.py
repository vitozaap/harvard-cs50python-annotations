from fuel import gauge, convert
import pytest


def test_empty():
    assert gauge(1) == "E"


def test_full():
    assert gauge(99) == "F"


def test_porcentage():
    assert gauge(50) == "50%"


def test_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_split():
    with pytest.raises(ValueError):
        convert("2:0")


def test_valid_int_return():
    assert convert("2/3") == 67


def test_invalid_division():
    with pytest.raises(ValueError):
        convert("2/1")


def test_negative_division():
    with pytest.raises(ValueError):
        convert("-1/2")
