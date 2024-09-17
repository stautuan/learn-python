"""
Implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format, and outputs
a table formatted as ASCII art using tabulate. Format the table using
the library’s grid format. If the user does not specify exactly one
command-line argument, or if the specified file’s name does not end
in .csv, or if the specified file does not exist, the program should
instead exit via sys.exit.
"""
# TODO: organize code 

import csv
import sys
from tabulate import tabulate


# sys.argv[1] == name of the CSV file
# import tabulate, use tabulate(table, headers, tablefmt="grid")
# if sys.argv[1] is None, if file is not a .csv, if file does not exist, then sys.exit()

# first open the CSV file

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_path = sys.argv[1]

if not file_path.endswith(".csv"):
    sys.exit("Not a CSV file")

menu = []
try:
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(list(row))

    print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
