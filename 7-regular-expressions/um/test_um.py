from um import count

def test_count():
    assert count("hello, um, world") == 1
    assert count("yummy") == 0
    assert count("Um, what is, um, your name?") == 2
