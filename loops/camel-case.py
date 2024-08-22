"""
Implement a program that prompts the user for the name of a
variable in camel case and outputs the corresponding name in
snake case. Assume that the user's input will indeed be in
camel case.
"""

camel_case = input("camelCase: ")
snake_case = ""

for c in camel_case:
    if c.isupper():
        snake_case += "_" + c.lower()
    else:
        snake_case += c
print(f"snake_case: {snake_case}")
