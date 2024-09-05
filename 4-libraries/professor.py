"""
Implement a program that:
- Prompts the user for a level, n. 
    - If user does not input 1, 2, or 3, prompt again.
- Randomly generates 10 math problems formatted as `X + Y = `,  wherein each of X and Y is a non-negative
  integer with n digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), 
  the program should output `EEE` and prompt the user again, allowing the user up to three tries in total
  for that problem. If the user has still not answered correctly after three tries, the program should output
  the correct answer.
- The program should ultimately output the user's score: the number of correct answer out of 10.
"""

# [x] prompt user for level
# [x] if level == 1 or 2 or 3, generate math problems
# [x] else prompt the user again
# [x] randomly generate 10 math problems
# [x] prompt user to solve the math problem
# [x] if answer is incorrect int / type, print EEE and prompt again (3 attempts)
# [x] after 3 attempts, print the correct answer
# [x] print user score

import random


def main():
    while True:
        try:
            level = get_level()

            if level in [1, 2, 3]:
                score = 0
                for _ in range(10):
                    x = generate_integer(level)
                    y = generate_integer(level)
                    answer = x + y
                    attempts = 0

                    while attempts < 3:
                        try:
                            user_answer = int(input(f"{x} + {y} = "))
                            if user_answer == answer:
                                score += 1
                                break
                            else:
                                print("EEE")
                                attempts += 1
                        except ValueError:
                            pass
                    if attempts == 3:
                        print(f"{x} + {y} = {answer}")
                print(f"Score: {score}")
                break
        except ValueError:
            pass


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
