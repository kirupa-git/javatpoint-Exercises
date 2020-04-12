try:
    import numpy as np
    print("Enter any 9 number range")
    # create a 3*3 matrix
    user_input1 = int(input("First Number:"))
    print(f"Suggestion :{user_input1+9}")
    user_input2 = int(input("Last Number:"))

    matrices1 = np.arange(user_input1, user_input2).reshape(3, 3)
    matrices2 = np.arange(user_input1, user_input2).reshape(3, 3)

    print(f"{matrices1},\n {matrices2}")

    sum_matrices = np.add(matrices1, matrices2)
    multiply_matrices = np.multiply(matrices1,matrices2)
    print(f"Sum of two same matrices :{sum_matrices}")
    print(f"Multiply of two same matrices :{multiply_matrices}")
    print(f"Transposed Matrix:{np.transpose(matrices1)}")
except ValueError:
    print("Enter a valid range of 3*3 numbers")

