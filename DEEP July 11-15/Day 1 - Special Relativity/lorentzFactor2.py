# import statements: let Python know what modules we want to use
# functions we use from these modules are prefaced with a prefix
# eg: np.sqrt

import numpy as np
import matplotlib.pyplot as plt


# c = 299792458 # speed of light
c  = 1 # speed of light: set to 1 for simplicity, first

# position, velocity, time in Bob's frame
x = 0.5
v = 0.5
t = 1


def calc_gamma(v):
	# function to calculate gamma (the Lorentz factor), given v
	# np.sqrt is a function from the numpy module which calculates the square root
	return 1/np.sqrt(1-(v/c)**2)

# disregard this function for the first exercise
def lorentz(t,x,v):
	# function to calculate lorentz transformation, given t, x, and v
	# note: you can call functions within functions
	g = calc_gamma(v) # calculate the Lorentz factor using the function above
	xt = g*(x-v*t) # calculate x'
	tt = g*(t-v*x/c**2) # calculate t'
	return tt, xt # return calculated vlaues

def lorentz_inv(tt,xt,v):
	g = calc_gamma(v)
	x = g*(xt + v*tt)
	t = g*(tt + v*xt/c**2)
	return t, x


print(lorentz(t,x,v))
######## INVARIANT INTERVAL


def calc_interval(dt,dx):
	return dx**2 - c**2*dt**2

print(calc_interval(1, 0.5))
print(calc_interval(np.sqrt(0.75), 0))