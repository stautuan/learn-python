"""
Implement a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded
to the nearest integer, how much fuel is in the tank. If, though, 1% or less
remains, output E instead to indicate that the tank is essentially empty. And if
99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt
the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions
like ValueError or ZeroDivisionError.
"""


def main():
    while True:
        fraction = input("Fraction: ")
        percentage = get_percentage(fraction)
        if percentage is not None:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
    

def get_percentage(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if x <= y and y != 0:
            return round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        pass


main()