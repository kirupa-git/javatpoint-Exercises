print("To Find Armstrong Number in an Interval")

least_input = int(input("Least Number:"))
max_input = int(input("Max Number:"))

range_numbers = range(least_input, max_input + 1)

# range of numbers
for number in range_numbers:
    # print(number)
    # check length of number
    length = 0
    duplicate_number = number
    checker = number
    while number > 0:
        length += 1
        number = number // 10
    # print(length)
    # separate digits in number
    output = []
    while duplicate_number > 0:
        rem = duplicate_number % 10
        duplicate_number = int(duplicate_number / 10)
        output.append(rem)
    result = []
    for output_number in output:
        result.append(output_number ** length)
    sum_result = sum(result)
    # print(sum_result,checker)
    if sum_result == checker:
        print(f"{checker}")



