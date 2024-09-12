# Implement a program that expects exactly one command-line argument, the
# name (or path) of a Python file, and outputs the number of lines of code
# in that file, excluding comments and blank lines. If the user does not
# specify exactly one command-line argument, or if the specified file’s name
# does not end in .py, or if the specified file does not exist, the program
# should instead exit via sys.exit.

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_path = sys.argv[1]

# endswith() finds a string that ends with a specified characer/s (".py")
if not file_path.endswith(".py"):
    sys.exit("Not a python file")

try:
    with open(file_path, "r") as file:
        lines = file.readlines()

    num_of_lines = 0
    for line in lines:
        # strip() removes leading and trailing whitespace
        # startswith() finds a string that starts with a specific character ("#"")
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            num_of_lines += 1

    print(num_of_lines)

except FileNotFoundError:
    sys.exit("File does not exist")


