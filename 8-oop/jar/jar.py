# deposit should add n cookies to the cookie jar.
# if it exceeds, deposit should raise a ValueError.

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        n = "🍪"
        return n * self.cookies

    def deposit(self, n):
        if n + self.cookies > self.capacity:
            raise ValueError("You have exceeded the cookie jar's capacity.")
        self.cookies += n

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError("There aren't that many cookies in the cookie jar.")
        self.cookies -= n

    @property
    def capacity(self):
        pass

    @property
    def size(self):
        pass