"""
Implement a program that:
    - prompts the user for a level, n (int)
    - prompts again if the user does not input a positive integer
    - randomly generates an integer between 1 and n, inclusive
    - prompts the user to guess that integer
        - if guess != positive int, prompt again
        - if guess < positive int, output "Too small!", and prompt again
        - if guess > positive int, output "Too large!", and prompt again
        - if guess == positive int, output "Just right!, and exit
"""

import random
import sys

def main():

    while True:
        try:
            level = int(input("Level: "))
            positive_int = random.randint(1, level)
            break
        except ValueError:
            pass

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < positive_int:
                print("Too small!")
            elif guess > positive_int:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            pass


if __name__ == "__main__":
    main()