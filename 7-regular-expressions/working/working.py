"""
Implement a function called `convert` that expects a `str` in any of the 12-hour formats below
and returns the corresponding `str` in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and
PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM
specifically.

Raise a `ValueError` instead if the input to `convert` is not in either of those formats or if
either time is invalid. But do not assume that someone's hours will start ante meridiem and end
post meridiem; someone might work late and even long hours (e.g. 5:00 PM to 9:00 PM)
"""

import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid time format")

    # Extract groups from the match
    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    if start_min is None:
        start_min = ":00"

    if end_min is None:
        end_min = ":00"

    # Convert to 24-hour format
    start_24 = to_24_hour(start_hour, start_min, start_period)
    end_24 = to_24_hour(end_hour, end_min, end_period)

    return f"{start_24} to {end_24}"

def to_24_hour(hour, minutes, period):
    hour = int(hour)
    minutes = minutes[1:] # remove the colon from minutes

    if hour < 1 or hour > 12 or int(minutes) < 0 or int(minutes) > 59:
        raise ValueError("Invalid time")

    if period == "AM":
        if hour == 12:
            hour = 0
    else: # if PM
        if hour == 12:
            hour = 12
        else:
            hour = hour + 12

    return f"{hour:02}:{minutes}"


if __name__ == "__main__":
    main()
