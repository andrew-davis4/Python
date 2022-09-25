# import statements: let Python know what modules we want to use
# functions we use from these modules are prefaced with a prefix
# eg: np.sqrt

import numpy as np
import matplotlib.pyplot as plt


# c = 299792458 # speed of light
c  = 1 # speed of light: set to 1 for simplicity, first

def calc_gamma(v):
	# function to calculate gamma (the Lorentz factor), given v
	# np.sqrt is a function from the numpy module which calculates the square root
	return 1/np.sqrt(1-(v/c)**2)


# 1000 points in the array
n = 1000
v = np.linspace(0, c, 1000) # create array for v here

gamma_v = calc_gamma(v) # call the function calc_gamma to calculate gamma_v

# uncomment to plot after calculating gamma_v

plt.plot(v, gamma_v) # plots v on horizontal axis, gamma_v on vertical axis
plt.title("Lorentz factor as a function of velocity (units of c)") # plot title
plt.xlabel('v') # x axis label
plt.ylabel('gamma_v') # y axis label
plt.show()