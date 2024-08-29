"""
Implement a program that prompts the user for a str in English and then outputs 
the “emojized” version of that str, converting any codes (or aliases) therein to 
their corresponding emoji.
"""

import emoji

def main():
    # prompt user for a string
    str = input("Input: ")
    # convert
    emojize = emoji.emojize(str, language='alias')
    print(f"Output: {emojize}")


if __name__ == "__main__":
    main()