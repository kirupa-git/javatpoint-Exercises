print("Hello Python")

print("Arithmetic operations(add,sub,multiply,div)")

operation = input("operation:" )
num1 = float(input("x:" ))
num2 = float(input("y:" ))

operation = operation.lower()

def arithmetic_operations(operation,num1, num2,):
    if operation == "add":
        return float(num1+num2)
    elif operation == "sub":
        return float(num1-num2)
    elif operation == "multiply":
        return float(num2*num1)
    elif operation == "div":
        return float(num1/num2)


Result = arithmetic_operations(operation, num1, num2, )
print(f"Result:{Result}")
