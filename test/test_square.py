from square import square
import pytest


""" 
# This is NOT a good testing practice
def test_square():
    try:
        # If true, not gonna do anything. But if false, throws an AssertionError
        assert square(2) == 4
        assert square(3) == 9
        print("Tests passed!")
    except AssertionError:
        print("Tests failed.")
"""


# Now I can run pytest to test it automatically for me, giving more useful information about the failure
# Its a good practice to have multiple stages and steps when testing some function.
# When you separate and have multiple tests, you can visualize better which tests are failing at once


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_zero():
    assert square(0) == 0


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_str_input():
    # Testing if something throws a specific error 
    with pytest.raises(TypeError):
        square("cat")
