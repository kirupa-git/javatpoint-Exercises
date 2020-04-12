print("Python Program to Sort Words in Alphabetic Order")

try:
    user_input = input("Enter words to sort:")
    split_input = user_input.split(" ")
    split_input.sort()
    for values in split_input:
        print(values)

except TypeError or NameError:
    print("Enter valid characters")
