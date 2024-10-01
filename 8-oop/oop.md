## Classes

In a class, we can invent our own data type and give them name.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

- `Student` is the class
- we initialize the class using the `__init__` method that takes the `name` and `house`

## raise

```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

- We check that a `name` is provided and a proper `house` is designated.
- We can create our own exceptions that alerts the programmer to a potential error created by the user called `raise`.
- In the case above, we `raise ValueError` with a specific error message.
