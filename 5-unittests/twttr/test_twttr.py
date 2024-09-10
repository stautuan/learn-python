from twttr import shorten


def test_lower():
    assert shorten("hello") == "hll"


def test_upper():
    assert shorten("AMAZING") == "MZNG"


def test_numbers():
    assert shorten("qutie23") == "qt23"


def test_punctuation():
    assert shorten("Inconcievable!") == "ncncvbl!"
