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
