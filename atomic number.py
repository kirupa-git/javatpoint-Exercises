print("To Check Armstrong Number")

user_input = int(input("is it armstrong number:"))
double_work = user_input

result = []
count = 0
while user_input > 0:
    count += 1
    rem = user_input % 10
    user_input = user_input // 10
    result.append(rem)
answer = []
for numbers in result:
    answer.append(numbers ** count)
final = sum(answer)
if final == double_work:
    print(f"entered number {double_work} is armstrong number")
elif final != double_work:
    print("Not a armstrong number")


