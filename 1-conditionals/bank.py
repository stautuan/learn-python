def main():
    greet = capital(input("Greeting: ").strip())
    if "Hello" in greet:
        print("$0")
    elif starts_with_h(greet):
        print("$20")
    else:
        print("$100")


def capital(text):
    return text.title()


def starts_with_h(text):
    return text[0] == "H"


main()
