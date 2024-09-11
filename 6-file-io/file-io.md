# File I/O

## open

This is a built-in function in Python that allows us to open a file so that we can read and write to it.

```python
name = input("What is your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```

`open`

- first argument is the name of the file we want to open
- second argument can be either `w`, which means we want to write to it. However, this will entirely rewrite the file each time we run and input something to our program. If this isn't what we intended to do, we can `a` append to it. This persists the data we have previously stored.

## with

This allows us to automate the closing of a file.

`readlines()` allows us to exclusively read from a file. We can also store the lines we've read into a variable in order to access them.

```python
with open("names.txt", "a") as file:
    lines = file.readlines()

for line in lines:
    print("hello", line)
```

However, we can simplify this like so:

```python
# we create an empty list in order to store the sorted names
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
```

- `rstrip()` removes extra line breaks or spaces at the end of each line
- `sorted()` sorts the list to ascending order
