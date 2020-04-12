print("Python program to print the duplicate elements of an array")

# Initialize array
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]
org_arr = []

print("original elements in given array: ")
for i in arr:
    if i not in org_arr:
        org_arr.append(i)
print(org_arr)

print("Removed elements in given array: ")

dup_arr=[]

for i in range(len(arr)):
    if arr[i] in arr[:i]:
        (dup_arr.append(arr[i]))


print(dup_arr)
