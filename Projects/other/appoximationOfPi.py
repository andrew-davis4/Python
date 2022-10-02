from random import random as r

total = 100000000
count = 0
# a = 100

b = 0
c = 0

for k in range(total):
    x = r()
    y = r()
    if x**2+y**2 <= 1:
        count += 1
    if count%1000000 == 0:
        print(count/1000000, "mil")

print('Pi is approximately', 4*count/total)