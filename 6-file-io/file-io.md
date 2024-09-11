# File I/O

## open

`open()` is a built-in function in Python. It opens a file so that we can read and write to it.

```python
name = input("What is your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```

- the first argument is the name of the file we want to open
- in the second argument, we want to specify what we want to do to the file we are opening. Some of the modes include `w`, when we want to write to it. However, this will entirely rewrite the file each time we run and input something to our program. If this isn't what we intended to do, we can `a` append to it. This persists the data we have previously stored.

## with

Sometimes, we forget to close the file. `with` allows us to automate the closing of a file.

`readlines()` allows us to exclusively read from a file. We then store the lines read into a variable so that we can access them.

```python
with open("names.txt", "a") as file:
    lines = file.readlines()

for line in lines:
    print("hello", line)
```

However, we can simplify this like so:

```python
# create an empty list in order to access the sorted names
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
```

- `rstrip()` removes extra line breaks or spaces at the end of each line
- `sorted()` sorts the list to ascending order

## CSV

"comma separated values"

Below is what our CSV file `students.csv` looks like.

```csv
Hermione,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin
```

```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

```

The above code reads our csv file. Notice that we used the `split(",")` function. It finds the comma, as we have specified, and splits the string into a list. Since there are two elements in a list, we store each in a variable called `name` and `house` respectively. Here is what it looks like:

```python
# [name, house]
["Hermione", "Gryffindor"]
["Harry", "Gryffindor"]
["Ron", "Gryffindor"]
["Draco","Slytherin"]
```

To sort this list:

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
```

To organize our data as dictionaries, we can modify it like so:

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
```

To sort a dictionary, we will use a `lambda` function, which is an anonymous function. Lambda functions are useful when the function will only be referenced once in our code.

`sorted()` takes another parameter `key` that specifies a function that will be used to determine the sorting order.

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
```

```python
# unsorted list
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]
```

The lambda function takes one parameter `student` and returns a list of a sorted students by "name" from the `student` dictionary.

```python
# sorted list
students = [
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
]
```
