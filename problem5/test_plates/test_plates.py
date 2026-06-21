from plates import is_valid


def test_plates_start():
    assert is_valid("22BB22") == False
    assert is_valid("B22") == False
    assert is_valid("BBBB22") == True


def test_length():
    assert is_valid("AAABB22") == False
    assert is_valid("A") == False


def test_ponctuation():
    assert is_valid("AA.B22") == False


def test_zero():
    assert is_valid("AAAA00") == False


def test_numbers_position():
    assert is_valid("AA22AA") == False


def test_whitespaces():
    assert is_valid("AA A22") == False
