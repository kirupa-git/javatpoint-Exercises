print("Python program to left rotate the elements of an array")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rotate = 3

for i in range(0, rotate):
    first = my_list[0]
    for j in range(0, len(my_list) - 1):
        my_list[j] = my_list[j + 1]
    my_list[-1] = first

for i in range(0, len(my_list)):
    print(my_list[i])
