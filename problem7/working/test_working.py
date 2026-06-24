import pytest
from working import convert


def test_no_minutes():
    result = "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == result
    assert convert("9:00 AM to 5 PM") == result
    assert convert("9 AM to 5:00 PM") == result

def test_omitting_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

def test_hours_out_of_range():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

def test_minutes_out_of_range():
    with pytest.raises(ValueError):
        convert("09:60 AM to 5 PM")
