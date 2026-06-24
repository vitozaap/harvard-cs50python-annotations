import pytest
from um import count
def test_um_mid_word():
    assert count("yummy") == 0
    assert count("yum") == 0


def test_um_count():
    assert count("hello, um, world") == 1
    assert count("hello, um world") == 1

def test_case_insensitive():
    assert count("UM") == 1
    assert count("Um") == 1
