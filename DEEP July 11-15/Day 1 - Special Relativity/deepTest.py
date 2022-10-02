from tkinter.tix import Y_REGION
import numpy as np

def time():
    y = 10000
    v = 0
    a = -9.8
    if v**2-2*a*y > 0:
        t = (-v-np.sqrt(v**2-2*a*y))/a
    else:
        t = 'invalid'
    print(t)
# time()
def expandedFormEquation():
    print('-- Given the vertex eqn: g(x-h)^2+k --')
    g = int(input("Enter the g value of the vertex eqn: "))
    h = int(input("Enter the h value of the vertex eqn: "))
    k = int(input("Enter the k value of the vertex eqn: "))

    expandedFormString = ""
    print(expandedFormString)
# expandedFormEquation()




# x = np.array([1,2,3])
# print(x)
# x -= 1
# print(x)


# y = np.arange(1, 10, 0.5)
# print(y)
# z = np.linspace(1, 10, 10)
# print(z)

c = 299792458



