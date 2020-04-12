import calendar

print("To Check Leap Year")

try:

    year_input = int(input(">"))

    if calendar.isleap(year_input) is True:
        print(f"Entered year {year_input} is Leap Year ")
    elif calendar.isleap(year_input) is False:
        print(f"Entered year {year_input} is not a  Leap Year ")

except ValueError:
    print("Entered value is not a Valid Year")





