import random
import sys

from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        f = random.choice(fonts)
        figlet.setFont(font=f)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "-font"]:
        f = sys.argv[2]
        if f in fonts:
            figlet.setFont(font=f)
    else:
        sys.exit("Invalid usage")


    s = input("Input: ")
    print(f"Output: {figlet.renderText(s)}")


if __name__ == "__main__":
    main()