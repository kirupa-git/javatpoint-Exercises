print("To print the elements of an array present on even position")
arr = [1, 2, 3, 22, 4, 2, 2, 7, 6, 4, 814, 8]

for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])

print("To print the elements of an array present on odd position")
for i in range(len(arr)):
    if i % 2 != 0:
        print(arr[i])

print("To print the largest element in an array")
maximum = arr[0]
for numbers in arr:
    if numbers > maximum:
        maximum = numbers
print(maximum)

print("To print the smallest element in an array")
least = arr[0]
for numbers in arr:
    if numbers < least:
        least = numbers
print(least)

print("To print the number of elements present in an array")
count = len(arr)
print(count)

print("To print the sum of all elements in an array")
addition = 0
for i in range(len(arr)):
    addition = addition + arr[i]
print(sum)

print("To right rotate the elements of an array")
print(arr)


def right_rotate(number):
    print(arr[-number % len(arr):]+(arr[:-number % len(arr)]))


right_rotate(2)

print("To sort the elements of an array in ascending order")
arr.sort()
print(arr)

print("To sort the elements of an array in descending order")
arr.sort(reverse=True)
print(arr)


