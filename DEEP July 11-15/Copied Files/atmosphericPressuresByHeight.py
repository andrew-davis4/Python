import numpy as np
import matplotlib.pyplot as plt

p0 = 100e3 # initial pressure in pascals
R = 287.058 # ideal gas constant
T = 300 # temperature in Kelvin
g = 9.81 # gravitational constant, m/s**2

zmax = 20e3 #m, maximum distance
dz = 1 # z increment (small compared to maximum distance)
z = np.arange(0,zmax,dz) # array of z values
p = np.zeros(len(z)) # array of zeros, to fill with z values
dpdz = np.zeros(len(z))

p[0] = p0 # set initial value (at ground)

k = g/(R*T) # value of k

# solve the equation in a for loop
for i in np.arange(len(z)-1):
    dpdz[i] = -k*p[i]
    p[i+1] = p[i] + dpdz[i]*dz

    

# uncomment to plot solution
# plt.plot(p,z)
# plt.title('Pressure vs. height')
# plt.xlabel('Pressure (Pa)')
# plt.ylabel('Height (m)')
# plt.show()

# z = p0**(-k*z)
# p_true = np.linspace(len(z))# calculate the true value here


# uncomment to compare with the true value
plt.plot(p,z)
# plt.plot(p_true,z)
plt.title('Pressure vs. height, comparison')
plt.xlabel('Pressure (Pa)')
plt.ylabel('Height (m)')
plt.show()