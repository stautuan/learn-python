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

## Decorators

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

   # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

- The `@property` turns the method `house` as a getter and a property of our class, which allows us to access the `house` attributes.
- It returns a value `self._house`.
- The underscore is a convention in Python that tells the other programmers working on this code that "This is an actual data storage and it shouldn't be accessed directly from outside the class." It's only for internal use.

Without underscore:

```python
@property
    def house(self):
        return self.house # This would cause recursion! It triggers to call the getter method again.
```

```python
@property
    def house(self):
        return self.house_value # This works fine
```

- The `@house.setter` sets the value of the house.
- If it's valid, it stores the value in `self._house`

## Class Methods

- `@classmethod` works with the **class** and not the **instances** of a class.
- Therefore it takes `cls` instead of `self`.
- `self` is like saying "This specific thing".
- `cls` is like saying "This type of thing".

```python
import random


class Hat:
    # there is no __init__ method because we don't need to instantiate a hat
    # because there's only ONE hat after all :)
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
```

Let's apply this to our previous example.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

   @classmethod
   def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
```

- We have remove the `get_student` function and applied its functionality to the `@classmethod`.
- We then called the `get` method with the class name `Student`.
