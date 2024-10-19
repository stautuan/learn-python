# Regular Expressions

```python
email = input("What's your email? ").strip()

if "@" in email:
    print("valid")
else:
    print("invalid")
```

- The `.strip()` removes the whitespace.
- As long as there is an `@` sign, the input will be `valid`.
- Error: If one inputs `@@`, it will also be `valid`.

Let's improve our program with `re` regular expressions. These are patterns that will help us validate if an email is formatted correctly, for example.

```
# list of symbols to create a regular expression
.   a (dot) matches a character, ex: 'a.c' = 'abc', 'a1c', 'a@c'
*   any amount of this including NONE at all, ex: 'ab*c' = 'ac', 'abbc', 'abbbbbc'
+   at least ONE of this, ex: 'ab+c' = 'abc', 'abbbbc' BUT NOT 'ac'
?   this means optional, 0 or 1 time, ex: 'ab?c' = 'ac', 'abc' BUT NOT 'abbc'
{m} this means the EXACT count, ex: 'a{3}' = 'aaa' BUT NOT 'aa'
{m,n} repetitions between m and n, ex: a{2,4} = 'aa', 'aaa', 'aaaa' BUT NOT 'aaaaa'
```

```python
import re

email = input("What's your email? ").strip()

if re.search(".+@.+.edu", email):
    print("valid")
else:
    print("invalid")
```

- If the input is `stacy@harvard.edu` it would be `valid`.
- If the input is `stacy@harvard?edu` it would be `valid`.

Let's improve that.

```python
import re

email = input("What's your email? ").strip()

if re.search(".+@.+\.edu", email):
    print("valid")
else:
    print("invalid")
```

Much better. We have utilized the "escape character" `\` to include the `.` before the `edu` as part of our string.

Let's further improve our program by using "raw strings" `r`.

```python
import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
	print("Valid")
else:
	print("Invalid")
```

```
^   the start of the string
$   the end of the string
r   raw string - string that don't format special characters
```

The raw string `r` is telling the compiler to treat each character as a single character, unlike `\n`, two characters that become one, is treated as a newline. Next, start the expression `^` that accepts all characters `.` and fills it at with at least one character `+` before and after the `@` symbol. Close it with `$`.

However if we type in `harry@@@hogwarts.edu` it is still `valid`. Let's continue to improve our program:

```python
import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
	print("Valid")
else:
	print("Invalid")
```

`harry@@@hogwarts.edu` it is now regarded as `invalid`.

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
