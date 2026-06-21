from bank import value


def test_not_greeting():
    assert value("Whats up?") == 100


def test_insensitivity_case():
    assert value("Hello") == 0 and value("hello") == 0
    assert value("Whats up") == 100 and value("whats up") == 100
    assert value("How are you") == 20 and value("how are you") == 20


def test_first_letter_h():
    assert value("how are you") == 20
