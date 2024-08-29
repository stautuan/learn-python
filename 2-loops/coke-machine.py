"""
Implement a program that prompts the user to insert a coin, one at a 
time, each time informing the user of the amount due. Once the user 
has inputted at least 50 cents, output how many cents in change the 
user is owed. Assume that the user will only input integers, and ignore 
any integer that isn't an accepted denomination.
"""

amount_due = 50
print(f"Amount Due: {amount_due}")

while amount_due > 0:
    coin = int(input("Insert Coin: "))

    if coin == amount_due or coin == 25 or coin == 10 or coin == 5:
        amount_due -= coin

        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
        else:
            print(f"Amount Due: {amount_due}")
    else:
        print(f"Amount Due: {amount_due}")
