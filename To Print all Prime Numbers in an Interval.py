import numbers
print("To Check Prime Number")

try:
    # to get input from user
    user_input = int(input(">"))
    while user_input >= 0:
        # range of numbers
        expected_number = range(2, user_input - 1)
        div_number = []
        for number in expected_number:
            div_number.append(user_input % number)
        if user_input == 0 or user_input == 1:
            print(f"Entered Number {user_input} is not Prime Number")
        elif 0 not in div_number:
            print(f"Entered Number {user_input} is Prime Number")
        elif 0 in div_number:
            print(f"Entered Number {user_input} is not Prime Number")
        user_input = int(input(">"))

except ValueError:
    print("Entered value is not a Valid number")
