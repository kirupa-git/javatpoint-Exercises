print("To Check if a Number is Positive, Negative or Zero")

try:
    number_input = int(input(">"))

    if number_input > 0:
        print(f"Entered value :{number_input} is positive")
    elif number_input == 0:
        print(f"Entered value :{number_input} is Zero")
    elif number_input < 0:
        print(f"Entered value :{number_input} is Negative")

except ValueError:
    print("Entered value is not a number")



