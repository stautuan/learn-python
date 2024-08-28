# Libraries

```python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```

- `random` is the module we like to import
- within the `random` module is the `choice()` function that takes a list
- we can also improve this by incorportating `from` which allows us to be _very specific_ of what we'd like to import

```python
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```

- `choice` is loaded explicitly into our program
- this saves system resources and potentially can make our code run faster

## Command-Line Arguments

What if we want to input values in the command line?

- `sys` us a module that allows us to take arguments at the command line.
- `argv` is a function within the `sys` module that allows us to learn what the user typed in the command line.

```python
import sys

print("hello, my name is", sys.argv[1])
```

- if we type `python name.py Stacy` into the terminal, its output will be `hello, my name is Stacy`
- `sys.argv[1]` is where `Stacy` is stored
- `sys.argv[0]` is `name.py`

Let's improve our program further.

Currently an error will occur when the user doesn't input a name. Here is how we can protect our program from this error:

```python
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
```

More refined error handling:

```python
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
```

Improve further by applying `sys.exit()`: the program can exit if an error arises

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
```
