def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            output = gauge(percentage)
            if output is not None:
                print(output)
                break
        except (ValueError, ZeroDivisionError):
            pass



def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round((x / y) * 100)



def gauge(percentage):
    if percentage is not None:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{percentage}%"


if __name__ == "__main__":
    main()
