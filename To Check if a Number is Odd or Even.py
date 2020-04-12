print("To Check if a Number is Odd or Even")

try:
    number_input = int(input(">"))

    if (number_input % 2) == 0:
        print(f"Entered number {number_input} is Even Number")
    elif (number_input % 2) != 0:
        print(f"Entered number {number_input} is Odd Number")


except ValueError:
    print("Entered value is not a number")


