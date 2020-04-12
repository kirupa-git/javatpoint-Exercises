print("To check if the given number is a Disarium Number")

user_input = input("Enter a Number:")


def disarium_number(number):
    number = int(user_input)
    given_number = user_input
    a = []
    for i in range(0, len(given_number)):
        a.append(int(i + 1))

    b = []
    for j in given_number:
        b.append(int(j))

    ab = []
    for i in range(len(a)):
        ab.append(b[i] ** a[i])

    if sum(ab) == number:
        print("entered Number is disarium number")
    else:
        print("entered Number is not a disarium number")



disarium_number(user_input)
