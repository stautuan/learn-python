"""
Implement a function that expects an IP address as input as a `str` and
then returns `True` or `False` if that input is valid IP address or not.
"""

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Repeat the same pattern with "." at the end 3 times
    regex = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    # Search the ip string if it matches the regex pattern
    if re.search(regex, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
