## Classes

In a class, we can invent our own data type and give them name.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

- `Student` is the class
- we initialize the class using the `__init__` method, which is a built-in function in Python, that takes the `name` and `house`

## raise

```python
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russel terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
```

- We check that a `name` is provided and a proper `house` is designated.
- We can create our own exceptions that alerts the programmer to a potential error created by the user called `raise`.
- In the case above, we raise `ValueError` with a specific error message.
- Classes have built-in functions called **method**. In this case, we have `__init__`, `__str__`, and `charm`.
- `__str__` is a built-in function in Python in which you can print the attributes of an object.
- `charm` is a method we have defined where specific cases have specific results.
