from plates import is_valid


def test_length():
    assert is_valid("C") == False
    assert is_valid("CS50") == True
    assert is_valid("OUTATIME") == False


def test_number():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
    assert is_valid("C5") == False


def test_zero():
    assert is_valid("CS05") == False


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("ILCS!") == False
