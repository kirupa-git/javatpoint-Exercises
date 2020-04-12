user_input = int(input("Enter a Number:"))


def factorial_fun(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_fun(n - 1)


print(factorial_fun(user_input))