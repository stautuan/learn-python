# __str__ should return a str with n "🍪", where n is the number of cookies in the jar
# if there are 3 cookies in the cookie jar there should be "🍪🍪🍪"

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self.capacity = capacity

    def __str__(self):
        n = "🍪"
        return n * self.cookies

    def deposit(self, n):
        pass

    def withdraw(self, n):
        pass

    @property
    def capacity(self):
        pass

    @property
    def size(self):
        pass