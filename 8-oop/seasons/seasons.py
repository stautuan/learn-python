"""
Implement a program that prompts the user for their date of birth in YYYY-MM-DD format
and then prints how old they are in minutes, rounded to the nearest integer, using English
words instead of numerals, just like the song from Rent, without any `and` between words.

Since a user might not know the time at which they were born, assume, for simplicity, that
the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current
time is also midnight. In other words, even if the user runs the program at noon, assume
that it’s actually midnight, on the same date. Use `datetime.date.today` to get today’s date.

Exit via `sys.exit` if the user does not input a date in YYYY-MM-DD format. Ensure that your
program will not raise any exceptions.
"""

# PROGRAM
# prompt user for date of birth in YYYY-MM-DD format
# print how old they are in minutes (rounded to nearest integer) using English words

# assume user was born at midnight on that date
# assume the time that the user runs the program is also midnight

# use datetime.date.today to get today's date.

# TODO:
# x Prompt the user with their date of birth.
# x Validate date format (YYYY-MM-DD)
# x Print age.
# 4. Find the difference between two dates.


from datetime import date


def main():
    date_of_birth = input("Date of Birth: ")

    if validate(date_of_birth):
        print(age(date_of_birth))
        print("Valid date format!")
    else:
        print("Invalid date")


def validate(date_str):
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False


def age(date_str):
    birth_year, birth_month, birth_day = date_str.split("-")
    present_year, present_month, present_day = str(date.today()).split("-")
    return int(present_year) - int(birth_year)


if __name__ == "__main__":
    main()
