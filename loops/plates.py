"""
Implement a program that prompts the user for a vanity plate and then
output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. Structure
your program per the below, wherein is_valid returns True if s meets all
requirements and False if it does not. Assume that s will be a str. You’re
welcome to implement additional functions for is_valid to call (e.g., one
function per requirement).
"""

import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # string must be a maximum of 6 and minumum of 2 characters
    if not 2 <= len(s) <= 6:
        return False
    
    # the first two characters must be letters
    if not s[0:2].isalpha():
        return False
    
    # it must not include any punctuation or spaces
    if any(char in string.punctuation for char in s) or " " in s:
        return False

    # if a string contains digits, it should only be at the end
    for char in s:
        if char.isdigit():
            index_of_digit = s.index(char)
            # this checks if the first digit is 0 or a digit is in the middle of two letters
            if s[index_of_digit] == "0" or not s[index_of_digit:].isdigit():
               return False
            break
    
    return True
        
         
main()
