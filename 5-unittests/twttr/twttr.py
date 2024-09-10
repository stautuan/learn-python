def main():
    text = shorten(input("Twitter: "))
    print(text)


def shorten(word):
    vowels = "aeiou"
    shorten_text = ""

    for w in word:
        if w.lower() not in vowels:
            shorten_text += w
    return shorten_text


if __name__ == "__main__":
    main()