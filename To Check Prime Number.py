
print("To Check Prime Number")


try:
    user_input = int(input(">"))

    if user_input > 0 and (user_input % user_input) == 1:
       print(f"Entered number: {user_input} is a Prime Number")
    elif user_input > 0 and (user_input % user_input) != 1:
        print(f"Entered number: {user_input} is not a Prime Number")

except ValueError:
    print("Entered value is not a Valid Year")





