def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours, minutes = int(hours), int(minutes)
    minutes = minutes / 60
    return hours + minutes


if __name__ == "__main__":
    main()
