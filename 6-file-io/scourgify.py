"""
Implement a program that:
    Expects the user to provide two command-line arguments:
        - the name of an existing CSV file to read as input, whose columns are
        assumed to be, in order, name and house, and
        - the name of a new CSV to write as output, whose columns should be, in
        order, first, last, and house.
    Converts that input to that output, splitting each name into a first name and
    last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first
cannot be read, the program should exit via sys.exit with an error message.
"""

import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    existing_file = sys.argv[1]
    new_file = sys.argv[2]
    read_file(existing_file)
    write_file(new_file)


"""
Open and read the existing file. Append each row to a new list as a dictionary with 
"name" and "house" as keys to easily reference them when we write a new file.
"""
students = []
def read_file(file_name):
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exist")


"""
Iterate to access the name and house of each student. Split the students' names to 
easily store them in variables for convenient access when placing them in their 
respective columns.
"""
def write_file(file_name):
    # "w" instead of "a" if we are only writing and not appending new data into the file
    with open(file_name, "w") as file:
        field_names = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for student in students:
            last, first = student["name"].split(", ")
            house = student["house"]
            writer.writerow({"first": first, "last": last, "house": house})


if __name__ == "__main__":
    main()