import numpy as np
import matplotlib.pyplot as plt


N = 10000 # number of steps
bound = 0.1 # min/max theta values
theta = np.linspace(-bound,bound,N) # array of beam angle values: ranges from -0.1 to 0.1 radians

lambd = 500e-9 # wavelength, 500 nm
a = 0.5e-3 # slit separation, 0.5 mm
b = 50e-6 # slit width, 50 micrometres
i0 = 1 # initial intensity

def calculate_a(a, wl, angle):
    return (np.pi*a/wl)*np.sin(angle) 
def calculate_b(b, wl, angle):
    return (np.pi*b/wl)*np.sin(angle)
def calculate_intensity(A, B, i0):
    return (i0*(np.sin(B)/B)**2*np.cos(A)**2)

# x = calculate_intensity(calculate_a(a, lambd, theta), calculate_b(b, lambd, theta), i0)
# y = theta
print(calculate_intensity(calculate_a(a, lambd, theta), calculate_b(b, lambd, theta), i0))

plt.plot(theta, calculate_intensity(calculate_a(a, lambd, theta), calculate_b(b, lambd, theta), i0))
# plt.xlabel("intensity")
# plt.ylabel("theta")
plt.show()


# define functions to calculate alpha and beta

# calculate final intensity, create a plot of intensity vs. theta
