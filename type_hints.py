# mypy can check if type hints are being respected
""" Docstrings can be used to documented automatically functions and modules in python. """
# "-> type" enforces the return type of the function
def meow(n: int) -> str:
    """
    :param n: Number of times to meow
    :type n: int
    :rtype: None
    :return: Print meow n times
    :raise TypeError: if n is not a number
    """

    for _ in range(n):
        print("meow")


# mypy will throw an error "mypy type_hints.py"
meow("2")

# mypy passes
meow(2)


