print("Python Program to Find HCF")

num1 = int(input("num1:"))
num2 = int(input("num2:"))

def hcf(num1,num2):
    if num2 > num1:
        num2,num1 = num1,num2
    answer  =[]
    for x in range(1, num1):
        if num1 % x == 0 and num2 % x == 0:
            (answer.append(x))
    print(f"HCF of two numbers : {answer[-1]}")


hcf(num1,num2)


