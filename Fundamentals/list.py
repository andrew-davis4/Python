numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers_list)
print(numbers_list[1])#outputs index 1 (or the number 2)
print(numbers_list[-2])#outputs index counting 2 from the end
print(numbers_list[0:3])#outputs particular range, not including index 3

print(len(numbers_list))#length of list

if 3 in numbers_list:
    print("Yes, 3 is in this list")
else:
    print("No, 3 is not in this list")


#Lists don't require datatypes:
mixed_list = ["apple", 1, "tree", 4.52]
print(mixed_list)

# Append: add item to the end of a list
mixed_list.append("orange")
print(mixed_list)
print(mixed_list[-1])

# 
