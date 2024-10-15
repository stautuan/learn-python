class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative.")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if n + self._cookies > self._capacity:
            raise ValueError("The cookie jar has exceeded the capacity.")
        self._cookies += n

    def withdraw(self, n):
        if self._cookies - n < 0:
            raise ValueError("There aren't that many cookies in the cookie jar.")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative.")
        if capacity < self._cookies:
            raise ValueError("Capacity cannont be negative.")
        self._capacity = capacity

    @property
    def size(self):
        return self._cookies

