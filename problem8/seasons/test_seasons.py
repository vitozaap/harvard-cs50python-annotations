from seasons import seasons, minutes
import pytest
from datetime import date


def test_reject_invalid_format():
    with pytest.raises(SystemExit):
        seasons("January 1, 1990")


def test_days_to_minutes():
    assert minutes(1) == 1440
    assert minutes(2) == 2880


def test_invalid_month():
    with pytest.raises(SystemExit):
        seasons("1990-13-31")


def test_invalid_day():
    with pytest.raises(SystemExit):
        seasons("1990-12-32")
