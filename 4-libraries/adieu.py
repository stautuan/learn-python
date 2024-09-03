"""
Implement a program:
    - prompts the user for names (one per line), until user inputs ctrl-d to exit
    - bid adieu to those names:
        - separate TWO names with ONE AND
        - separate THREE names with two commas and ONE AND
"""

import inflect
import sys

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print("")
            print(f"Adieu, adieu, to {p.join(names)}")
            sys.exit()


if __name__ == "__main__":
    main()
