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
        print("Amount Due: 50")
