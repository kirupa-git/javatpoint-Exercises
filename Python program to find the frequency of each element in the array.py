print("Python program to find the frequency of each element in the array")
list_items = [1, 2, 3, 3, 2, 1,0]
# convert to set
result = {}
for i in list_items:
    result[i] = list_items.count(i)
print(result)
