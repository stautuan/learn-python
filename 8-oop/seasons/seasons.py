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

# TODO:
# x Prompt the user with their date of birth.
# x Validate date format (YYYY-MM-DD)
# x Print age.
# x Find the difference between two dates using timedelta.
# x Convert minutes to words.

import inflect
import sys

from datetime import date


def main():
    date_of_birth = input("Date of Birth: ")

    if not validate(date_of_birth):
        sys.exit("Invalid date")

    try:
        minutes = calculate_minutes(date_of_birth)
        words = minutes_to_words(minutes).capitalize()
        print(f'{words} minutes')
    except ValueError as e:
        sys.exit(str(e))


def validate(date_str):
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False


def calculate_minutes(date_str):
    """Calculate age in minutes from birth date to today."""
    birth_date = date.fromisoformat(date_str)
    today = date.today()

    # Check if birth date is in the future
    if birth_date > today:
        raise ValueError("Birth date cannot be in the future")

    # Calculate days between dates and convert to minutes using timedelta
    days = (today - birth_date).days
    return days * 24 * 60


def minutes_to_words(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="")


if __name__ == "__main__":
    main()
