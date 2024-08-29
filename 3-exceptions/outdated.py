"""
Implement a program that prompts the user for a date, anno Domini, in
month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein
the month in the latter might be any of the values in the list below. Then
output that same date in YYYY-MM-DD format. If the user's input is not a
valid date in either format, prompt the user again. Assume that every month
has no more than 31 days; no need to validate whether a month has 28, 29, 30,
or 31 days.
"""

def main():
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)
                if is_valid_date(m, d):
                    outdated_date(y, m, d)
                    break
            elif "," in date:
                m, d, y = date.split(" ")
                m = int(month.index(m)) + 1
                d = int(d.replace(",", ""))
                y = int(y)
                if is_valid_date(m, d):
                    outdated_date(y, m, d)
                    break
        except (EOFError, ValueError):
            pass


def is_valid_date(month, day):
    return 1 <= month <= 12 and 1 <= day <= 31


def outdated_date(year, month, day):
    print(f"{year}-{month:02}-{day:02}")


main()