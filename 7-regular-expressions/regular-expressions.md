# Regular Expressions

These are patterns that will help us validate if an email is formatted correctly, for example.

There is a library in Python, `re` (regular expressions), that can help us validate emails using the regular expression pattern we are looking for.

```python
import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu", email):
	print("Valid")
else:
	print("Invalid")
```

## Extracting User Input

`sub` is a method that allows us to substitute a pattern with something else.

```python
re.sub(pattern, repl, string, count=0, flags=0)
```

- `pattern` regex we are looking for
- `repl` the string we can replace with
- `string` is what we want to do the substitution on.

```python
import re

url = input("URL: ").strip()

if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
print(f"Username: {username}", matches.group(1))
```

- The `?` is to make the `https://`, `s`, or `www.` optional
- The `[a-z0-9_]+` tells the compiler that only expect `a-z`, `0-9`, and `_` as part of the regular expression. The `+` indicates that we are expecting one or more characters.
