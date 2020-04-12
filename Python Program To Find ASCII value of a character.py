try:
    input_letter = input("Enter a Letter:")


    def ascii_list(input_letter):
        sd = ord(input_letter)
        print(f"Ascii value of {input_letter} is {sd}")


    ascii_list(input_letter)

except TypeError:
    print("Enter a valid character")
