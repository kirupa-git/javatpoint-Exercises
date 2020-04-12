print("to Print all Prime Numbers in an Interval")

least_number = 4
highest_number = 100

range_number=range(least_number, highest_number+1)

for numerator in range_number:
    if numerator > 1:
        for denominator in range(2, numerator):
            if (numerator % denominator) == 0:
                break
        else:
            print(numerator)




















