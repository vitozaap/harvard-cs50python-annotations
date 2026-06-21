from hello import say_my_name
import pytest


def test_invalid_arguments():
    # "With" is a block of code that ensures that, if fails, nothing is going to break. It runs __enter__ and __exit__ methods of the provided context.
    with pytest.raises(ValueError):
        say_my_name("Victor")


# Its a good practice to not have a lot of side effects into a function, because it makes it less testable
def test_valid_arguments():
    assert say_my_name("Victor Santos") == "firstname: Victor \nlastname: Santos"
