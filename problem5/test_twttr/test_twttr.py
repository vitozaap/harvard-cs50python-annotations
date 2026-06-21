from twttr import shorten
import pytest


def test_shorten():
    assert shorten("Test") == "Tst"


def test_uppercase():
    assert shorten("TEST") == "TST"


def test_numbers():
    assert shorten("Test123") == "Tst123"


def test_ponctuation():
    assert shorten("Test.") == "Tst."
