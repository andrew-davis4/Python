from os import system
import random


studentList = {
    "Grade12 A": 12,
    "Grade12 B": 12,
    "Grade12 C": 12,
    "Grade12 D": 12,
    "Grade12 E": 12,
    "Grade11 A": 11,
    "Grade11 B": 11,
    "Grade11 C": 11,
    "Grade11 D": 11,
    "Grade11 E": 11,
    "Grade10 A": 10,
    "Grade10 B": 10,
    "Grade10 C": 10,
    "Grade10 D": 10,
    "Grade10 E": 10,
    "Grade9 A": 9,
    "Grade9 B": 9,
    "Grade9 C": 9,
    "Grade9 D": 9,
    "Grade9 E": 9
}

system("cls") #clear terminal
placeholder = list(studentList.items())
# print(placeholder)
random.shuffle(placeholder) #now the dictionary of students in randomized
placeholder.append(placeholder[0])
print()
print(placeholder)

studentGotchaOrder = []

print()
for index in placeholder:
    studentGotchaOrder.append(index)
studentGotchaOrder.pop(0)


print(studentGotchaOrder)


studentList = dict(placeholder)
print()
# print(studentList)





