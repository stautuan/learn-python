import pytest

from jar import Jar


def test_init():
    # test default capacity
    jar = Jar()
    assert jar.capacity == 12

    # test custom capacity
    jar = Jar(20)
    assert jar.capacity == 20

    # test invalid capacity
    with pytest.raises(ValueError):
        Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    jar.withdraw(12)
    assert str(jar) == ""


def test_deposit():
    jar = Jar()

    # deposit within capacity
    jar.deposit(5)
    assert jar.size == 5

    # deposit that reaches capacity
    jar.deposit(7)
    assert jar.size == 12

    # deposit that exceeds capacity
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)

    # withdraw within available cookies
    jar.withdraw(3)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0

    # withdraw more than available cookies
    with pytest.raises(ValueError):
        jar.withdraw(1)
