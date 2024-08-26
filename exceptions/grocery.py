"""
Implement a program that prompts the user for items, one per line, until
the user inputs control-d (which is a common way of ending one's input to
a program). Then output the user's grocery list in all uppercase, sorted
alphabetically by item, prefixing each line with the number of times the
user inputted that item. No need to pluralize the items. Treat the user's
input case-insensitively.
"""


def main():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            print("\n")
            # items() returns a list of tuples
            # the list is sorted alphabetically by keys
            for key, value in sorted(grocery_list.items()):
                print(value, key)
            break


main()