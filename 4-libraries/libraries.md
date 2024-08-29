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

## Packages

One of the reasons why Python is so popular is because of its powerful third-party libaries called "packages". These packages can be installed using a package manager called `pip`. One of these packages that we will use for this example is `cowsay`, a well-known package that allows a cow to talk to the user.

```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
```

## APIs

- APIs allows us to connect to the code of others
- `requests` is a package that allows our program to behave as a web browser would
- For this example, we will use Apple iTunes' API

```python
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# based on Apple iTunes' documentation, we can fetch the
# data of a song we are requesting to get using this URL
# the output of this request is a JSON file
response = request.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
```

- `entity=song` specifies that the search is for songs
- `limit=1` the response should contain 1 song
- `term=` is the term we are searching for that is stored in `sys.argv[1]`

The output is quite dizzying tho! Let's make it readable by importing the JSON library.

```python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = request.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

# implement json.dumps() to utilize indent to make the output more readable
print(json.dumps(response.json(), indent=2))
```

Now, let's get the `trackName` of this JSON file

```python
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = request.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
```

We have stored the JSON response in `o`. Then iterate through it and print the `trackName`. Notice that we have set the limit to `50`, which means it will output 50 songs, as we specified from `entity=song`.
