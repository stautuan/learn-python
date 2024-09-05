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
# [ ] prompt user to solve the math problem
# [ ] if answer is incorrect int / type, print EEE and prompt again (3 attempts)
# [ ] after 3 attempts, print the correct answer
# [ ] print user score

import random


def main():
    while True:
        try:
            level = get_level()
            score = 0
            if level == 1 or level == 2 or level == 3:
                for _ in range(10):
                    try:
                        x = generate_integer(level)
                        y = generate_integer(level)
                        answer = x + y

                        user_answer = int(input(f"{x} + {y} = "))
                        if user_answer == answer:
                            score += 1
                        else:
                            print("EEE")
                    except ValueError:
                        print("EEE")
            print(score)
        except ValueError:
            pass


def get_level():
    return int(input("Level: "))


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
