# Unit Tests

## assert

This is a command that tells the compiler that something is true.

```python
from calculator import square


def main():
	test_square()


# compiler will output nothing if the code works as intended
def test_square():
	assert square(2) == 4
	assert square(3) == 9


if __name__ == "__main__":
	main()

```

## pytest

This is a third-party library that allows us to unit test our program.

Utilize it by installing `pip3 install pytest`.

To run the program: `pytest test-calculator.py` (the second argument is the name of the test file we want to run).

We can also utilize the functions within the `pytest` library such as `pytest.raises`, a function that allows us to express that we are expecting an error to be raised if the user inputs the wrong value.
