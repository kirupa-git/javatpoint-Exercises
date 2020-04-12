


userinput = int(input("Decimal Number:"))

def conversion_type(userinput):
    return print(f"Binary Number :{bin(userinput)} \n "
                f"Octal Number:{oct(userinput)} \n"
                f"Hexadecimal Number:{hex(userinput)}" )

conversion_type(userinput)