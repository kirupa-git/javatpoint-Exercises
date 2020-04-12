print("Python program to copy all elements of one array into another array")
# method 1

my_list = [1, 2, 3, 4, 5, 6, 2, 3]
dup_list = my_list.copy()
print(f"\noriginal list :\n{my_list}\n id : {id(my_list)}\n\n "
      f"Copied list:\n{dup_list} id:{id(dup_list)} ")

# method 2
duplicate_list = []
for items in my_list:
    duplicate_list.append(items)
print(duplicate_list)

