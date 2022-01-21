# lists are like arrays

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

# .append(): add item to the end of a list
mixed_list.append("orange")
print(mixed_list)

print(mixed_list[0])
print(mixed_list[-1])

# .insert(): insert item to specified index and moves the rest
mixed_list.insert(1, "banana")
print(mixed_list)

# replaces the item in the specified index with a new item
mixed_list[0] = "pear"
print(mixed_list)

# .remove(): removes specific known item (by name)
mixed_list.remove("tree")
print(mixed_list)

# .pop(): removed specified index, or the last item if index is not specified
mixed_list.pop(0)
print(mixed_list)

# --- ITERATE --- (print the list one at a time using for loops)

for i in range(len(numbers_list)):
    print(numbers_list[i])

print("-------------------")

for number in numbers_list:
    print(number)

# clear entire list
mixed_list.clear()
print(mixed_list)

# .copy(): to make a copy of the list
new_numbers_list = numbers_list.copy()
print(new_numbers_list)

print("")

# .sort(): sorts either numbers in order smallest to largest or words/letters in alphabetical order (BUT IT CHANGES THE LIST)
list1 = [3, 6, 1, 4, 3]
list1.sort()
print(list1)


list2 = sorted(list1) #this makes a copy then sorts it
print(list2)

##list3 = sorted()
##print(list3)


##------- COMBINING LISTS -------##
print("")

list4 = [1, 2]
list5 = ['a', 'b']
list6 = list4+list5 ##(same as .extend())
print(list6)

list4.extend(list5) ##(same as listA + listB)
print(list4)

list4.append(list5) ##(DIFFERENT - (nested list) adds the ENTIRE list as ONE element in the other list)
print(list4)
print(list4[4]) ## this is a whole list even though it is an element of the previous list


## --- TUPLE --- ##
## Unchangeable list:

fruit_tuple = ("apple", "banana", "cherry")
print(fruit_tuple)
print(fruit_tuple[1])
print(fruit_tuple[-1])
print(fruit_tuple[0:2]) #elements 0 to 2 (apple, banana, cherry) not including element 2 (cherry)

## fruit_tuple[1] = "appricot" (results in: TypeError: 'tuple' object does not support item assignment)

print("")
fruit_set = {"grape", "watermelon", "peach"} ## set doesn't duplicate items (if you add two 'apple', it will only who one), and it doesn't care about order:

fruit_set.add("orange") ## doesn't care where, it puts it in random spot
print(fruit_set)

## if you care about order, you need to sort it after adding:
## fruit_set.sort() (results in error - doesn't work for object 'set')
print(sorted(fruit_set))

fruit_set_sorted = sorted(fruit_set)
print(fruit_set_sorted)




