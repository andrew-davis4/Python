import numpy as np
import matplotlib.pyplot as plt

def logistic(x_n, r):
    # given r and x_n, calculate x_(n+1) based on the logistic map
    return r*x_n*(1-x_n)

n = 40 # number of iterations
r = 4.002897999 #r: growth/decay parameter; between 0 and 4
x0 = 0.4 # initial x: between 0 and 1

x = np.zeros(n)     # initialize array

x[0] = x0         # assign initial condition to first element of array

print(x) # what do you see here?

# iterate to calculate the values of the logistic map

for i in range(1,n):
	x[i] = logistic(x[i-1], r) # assign a value here

# create plots of the result (uncomment below later)
# plt.plot(x) # plot x
plt.show() # show the plot

y = np.arange(0,1,0.01)

plt.plot(x[:-1],x[1:],'.') # poincare plot
plt.plot(y, r*(y-y**2))
plt.show()