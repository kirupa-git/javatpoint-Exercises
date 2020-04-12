print("Python Program to Find LCM")

num1 = int(input("num1:"))
num2 = int(input("num2:"))


def lcm2(num1,num2):
    if num1 > num2:
        num1,num2 = num2,num1
#(num2 = largest of two numbers, multiplication for max of number, steps)
    for x in range(num2, num1 * num2 +1, num2):
        if x % num1 == 0:
            return print(x)


lcm2(num1,num2)






