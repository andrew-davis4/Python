# this script is in continuation of: colatzConjecture.py
# graphs the total stopping time of an integer put through the colatz conjecture for each integer 1-100

import matplotlib.pyplot as plt, numpy as np

fig, ax = plt.subplots()
j = 3

# isNumberInvalid = True
# while isNumberValid:

# number = int(input("Enter a number: "))
number = 3
i = 3
y = [0, 1, 2]
x = [0, 1, 2]

while j<100:
    k = 0
    while number!=1:
        if number%2==0:
            number = number/2
        else:
            number = number*3+1
        k += 1
    k += 1

    y.append(k)
    x.append(j)
    j += 1
    i += 1
    number = i

# #--gridlines and ticks--
# min_x = 0
# max_x = max(x)+10
# step_x = max(x)
# min_y = 0
# max_y = max(y)+11
# step_y = (max(y)+(max(y)%10))/10
# ax.set_xticks(np.arange(min_x, max_x, step=step_x))
# ax.set_yticks(np.arange(min_y, max_y, step=step_y))

# --axis labels--
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y)

# print("\"Hailstone\" Peak: ",max(y))
# print("Total stopping time: ",i)

# w = [1,2,3]
# z = [1,2,3]
# plt.plot(w,z)

# graph = input("Would you like to graph the data above? (y/n) ")
# if graph == "y":
#     print("Graphing...")
#     plt.show()
# else:
#     print("Have a good day!")

print(x, "\n", y)

plt.show()
