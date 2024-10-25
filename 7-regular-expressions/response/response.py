"""
Implement a program that prompts the user for an email address via `input`
and then prints `Valid` or `Invalid`, respectively, if the input is a
syntatically valid email address. You may not use `re`. And do not validate
whether the email address's domain name actually exists.
"""

from validator_collection import validators, errors

def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        email_address = validators.email(s)
        if email_address:
            return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
