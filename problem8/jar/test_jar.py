from jar import Jar
from unittest.mock import Mock
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar.capacity = 10
    assert jar.capacity == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2


def test_withdraw():
    jar = Jar()

    def side_effect(arg):
        jar._size = arg

    jar.deposit = Mock(side_effect=side_effect)
    jar.deposit(1)
    jar.deposit.assert_called_once_with(1)
    jar.withdraw(1)
    assert jar.size == 0


def test_deposity_constraint():
    jar = Jar(1)
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw_constraint():
    jar = Jar(1)
    with pytest.raises(ValueError):
        jar.withdraw(2)
