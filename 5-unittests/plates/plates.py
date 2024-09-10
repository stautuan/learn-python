import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not 2 <= len(s) <= 6:
        return False

    if not s[0:2].isalpha():
        return False

    if any(char in string.punctuation for char in s) or " " in s:
        return False

    for char in s:
        if char.isdigit():
            index_of_digit = s.index(char)
            if s[index_of_digit] == "0" or not s[index_of_digit:].isdigit():
               return False
            break

    return True


if __name__ == "__main__":
    main()
