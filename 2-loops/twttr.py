"""
Implement a program that prompts the user for a str of text and
then outputs that same text but with all vowels (A, E, I, O, U)
omitted, whether inputted in uppercase or lowercase.
"""

text = input("Twitter: ")

vowels = "aeiou"
short_text = ""

for t in text:
    if t.lower() not in vowels:
        short_text += t

print(f"Output: {short_text}")
