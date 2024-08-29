def main():
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
    if answer == "42" or convert(answer) == "fortytwo":
        print("Yes")
    else:
        print("No")


def convert(text):
    return text.lower().replace("-", "").replace(" ", "")


main()
