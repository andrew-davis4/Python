# /*

# Simple Collatz Conjecture Script

# Date Started: Aug 9th, 2021 (on repl.it https://replit.com/@ANDREWDAVIS44/3n1-script#Main.java)
# Adapted from java to python: April 30th, 2022
# Last updated: May 3rd, 2022

# Author: Andrew Davis

# *Enters any integer (n), if odd; applies 3n+1, if even; applies n/2, and repeats this cycle until reaching a 4-2-1 loop.

# **Additional Data Collected: Total Stopping Time (TST) - Highest "Hailstone" Peak

# */

import matplotlib.pyplot as plt, numpy as np

fig, ax = plt.subplots()

# isNumberInvalid = True
# while isNumberValid:

number = int(input("Enter a number: "))

x = [0]
y = [number]
i = 0

while number>1:
    if number%2==0:
        number = number/2
        i += 1
        y.append(number)
        x.append(i)
    else:
        number = number*3+1
        i += 1
        y.append(number)
        x.append(i)

min_x = 0
max_x = max(x)+10
step_x = max(x)
min_y = 0
max_y = max(y)+11
step_y = (max(y)+(max(y)%10))/10
ax.set_xticks(np.arange(min_x, max_x, step=step_x))
ax.set_yticks(np.arange(min_y, max_y, step=step_y))

plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y)

print("\"Hailstone\" Peak: ",max(y))
print("Total stopping time: ",i)

# w = [1,2,3]
# z = [1,2,3]
# plt.plot(w,z)

graph = input("Would you like to graph the data above? (y/n) ")
if graph == "y":
    print("Graphing...")
    plt.show()
else:
    print("Have a good day!")