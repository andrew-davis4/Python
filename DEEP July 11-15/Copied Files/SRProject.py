# Import the relevant modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an


## physical parameters
k = 12. #spring constant (N/m)
m = 1. #mass (kg)
c = 2.998792458e8 #speed of light (m/s)
n = 40001 #number of steps
t_tot = 20. # total time simulated
dt = t_tot/(n-1) #time step (s)

# v1 = 0.8*c
# v2 = -0.8*c
# dx = 4 # light years

## initial conditions
x_0 = 8.65e8 # Initial position (m)
v_0 = 0. # Initial velocity (m/s)

## initialize arrays
t = np.linspace(0.,t_tot,n) # Array of 20001 points with start time of 0.s and end time of 20.s
x = np.zeros(n) # Position Array
v = np.zeros(n) # Velocity Array
t_acc = np.zeros(n) # Array of time spent in spaceship
x_cla = np.zeros(n) # Classical approximation of position array
v_cla = np.zeros(n) # Classical approximation of velocity array

## set initial positions and initial velocities in arrays
x[0] = x_0
x_cla[0] = x_0
v[0] = v_0
v_cla[0] = v_0

# dx = 0.1

def gamma(v):
    return 1/np.sqrt(1-v**2/c**2)

## solve the ODE for the classical harmonic oscillator and the
## relativistic harmonic oscillator
for i in np.arange(n-1):
    v[i+1] = v[i] - k*x[i]/(m*gamma(v[i])**3)*dt
    x[i+1] = x[i] + v[i]*dt

for i in np.arange(n-1):
    v_cla[i+1] = v_cla[i] - k*x_cla[i]*dt
    x_cla[i+1] = x_cla[i] + v_cla[i]*dt


# make plots of the relativistic and classical positions and velocities vs.
# time
plt.figure(1) #Plot following in first window

plt.subplot(221) # Plot in first of four frames
plt.plot(t,x, color='orange') #Plot relativistic position vs time
plt.xlabel('time (s)')
plt.ylabel('relativistic position (m)')
plt.title('relativistic position vs time')

plt.subplot(222) # Plot in second of four frames
plt.plot(t,v, color='orange') # Plot relativistic velocity vs time
plt.xlabel('time (s)')
plt.ylabel('relativistic velocity (m/s)')
plt.title('relativistic velocity vs time')

plt.subplot(223) # Plot in third of four frames
plt.plot(t,x_cla, color='green')  # Plot position (with classical approx.) vs time
plt.xlabel('time (s)')
plt.ylabel('classical position (m)')
plt.title('position (with classical approx.) vs time')

plt.subplot(224) # Plot in fourth of four frames
plt.plot(t,v_cla, color='green') # Plot velocity (with classical approx.) vs time
plt.xlabel('time (s)')
plt.ylabel('classical velocity (m/s)')
plt.title('velocity (with classical approx.) vs time')

plt.subplots_adjust(hspace=0.3)

plt.show() # show all 4 diagrams

## code for animation comparing positions
fig = plt.figure()
plt.xlabel('time (s)')
plt.ylabel('position (relativistic vs. classical approx.) (m)')
plt.title('position (relativistic vs. classical approx.) vs time')

ax = plt.axes(xlim=(0,t_tot),ylim=(-9e8,9e8))

line1, = ax.plot([],[])
line2, = ax.plot([],[])

numsteps = len(t)
# print(numsteps)

t = t[::100]
x = x[::100]
x_cla = x_cla[::100]

def init():
    line1.set_data([],[])
    line2.set_data([],[])
    return line1, line2,

def animate(i):
    line1.set_data(t[:i], x_cla[:i])
    line2.set_data(t[:i], x[:i])
    return line1, line2,

anim = an.FuncAnimation(fig, animate, init_func=init, frames=(numsteps - 1), interval=1)
plt.show()

### Second Animation for comparing velocities (doesn't work)

# fig2 = plt.figure()

# ax2 = plt.axes(xlim=(0,t_tot),ylim=(-9e9,9e9))

# line3, = ax.plot([],[])
# line4, = ax.plot([],[])

# t = t[::100]
# v = v[::100]
# v_cla = v_cla[::100]

# def init2():
#     line3.setdata([],[])
#     line4.setdata([],[])
#     return line3, line4,

# def animate2(i):
#     line1.set_data(t[:i], v_cla[:i])
#     line2.set_data(t[:i], v[:i])
#     return line3, line4,
    
# anim2 = an.FuncAnimation(fig2, animate, init_func=init, frames=(numsteps - 1), interval=1)

# plt.show()