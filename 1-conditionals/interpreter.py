def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x, z = int(x), int(z)
    if y == "+":
        print(add(x, z))
    elif y == "-":
        print(subtract(x, z))
    elif y == "*":
        print(multiply(x, z))
    elif y == "/":
        print(divide(x, z))


def add(x, z):
    return round(float(x + z), 1)


def subtract(x, z):
    return round(float(x - z), 1)


def multiply(x, z):
    return round(float(x * z), 1)


def divide(x, z):
    return round(float(x / z), 1)


main()
