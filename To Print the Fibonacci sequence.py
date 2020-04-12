print("To Print the Fibonacci sequence")

target_input = int(input("Target Number:"))

a = 0
b = 1
# Target Number
while b <= target_input:
    print(b)
    a, b = b, a + b

# How many Terms?
term_input = int(input("How many Terms you want:"))

x,y =0,1
number_terms = 2

if number_terms == 0:
    print("Enter valid Terms")
elif number_terms == 1:
    print(f"{term_input}")
else:
    while number_terms <= term_input:
        print(y)
        x,y = y, x+y
        number_terms += 1




