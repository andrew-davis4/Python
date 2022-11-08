import numpy as np
import matplotlib.pyplot as plt

# physical parameters
m = 4.4e-3 # mass: 4.4 g = 4.4e-3 kg
L = 20e-2 # length of rod/string: 20 cm = 2e-1 m 
g = 9.81 # m/s**2, gravitational acceleration
n = 20001 # number of steps
t_tot = 10. # total time simulated (seconds)
dt = t_tot/(n-1) #time step (s)

# constant k (to simplify)
k = g/L

# initial angle in degrees
init_deg = 10

## initial conditions
h_0 = init_deg*np.pi/180 # initial angle: convert degrees to radians
w_0 = 0. # Initial angular velocity (rad/s)

## initialize arrays
t = np.linspace(0.,t_tot,n) # Array of n points with start time of 0 s and end time of 20 s
h = np.zeros(n) # angle array
w = np.zeros(n) # angular velocity array


## set initial positions and initial velocities in arrays
h[0] = h_0
w[0] = w_0

## solve the ODE for the pendulum
for i in range(n-1):
    # simple pendulum: linear ODE
    w[i+1] = w[i] - k*h[i]*dt # update angular velocity with angular acceleration
    h[i+1] = h[i] + w[i+1]*dt # update angle with angular velocity

plt.plot(t,h, '-', color='purple') # plot of h over time
plt.title('Angle vs. time')
plt.ylabel('h (angle, radians)')
plt.xlabel('Time (seconds)')
# plt.show() # uncomment this to view on two seperate graphs
#
plt.plot(t,w, color='pink') # plot of angular velocity, w, over time
plt.title('Angular velocity vs. time')
plt.ylabel('Angular velocity (radians/second)')
plt.xlabel('Time (seconds)')
plt.show()


# # maximum velocity
# # linear velocity = angular velocity * radius
# vmax = 
# print('the maximum velocity is {} m/s'.format(vmax))

# # conservation of energy

# # kinetic
# K = 

# # grav. potential
# U = 


# plt.plot(K)
# plt.plot(U)
# plt.plot(K+U)
# plt.show()