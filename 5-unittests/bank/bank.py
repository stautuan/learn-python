def main():
    amount = value(input("Greeting: ").capitalize())
    print(f"${amount}")


def value(greeting):
    if "Hello" in greeting:
        return 0
    elif greeting[0] == "H":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
