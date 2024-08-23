# Exceptions

Exceptions are things that go wrong within our coding.

## Runtime Errors

- They are created by unexpected behavior within our code.
- As programmers, we should be defensive to ensure that our users are entering what we expected.
- Create "error handling" to ensure the user behave as we intend.

## try

`try` and `except` are ways of testing user input before something goes wrong.

```python
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

If we run this code and type in `cat` an error will produce to the user: `x is not an integer`.

## else

Let's improve our code further with `else

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

Let's improve even further. If our user does not cooperate, the current program simply ends. That is not good. Let's use a loop instead. Keep prompting for `x` until the user cooperates 🤪

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```

If the user supplies the incorrect input, we keep producing the error message, and only `break` and stop the loop once the user succeeds in supplying the correct input.
