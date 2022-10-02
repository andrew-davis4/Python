import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an


# soccer player position vs. time data was taken from real data at
url = 'http://home.ifi.uio.no/paalh/dataset/alfheim/'

# the line of code below loads values from the text file player_pos.txt
# be sure to download this file from the Google Drive and keep it
# in the same folder as this script!
t, x, y = np.loadtxt('player_pos.txt')
# t is time, and x and y are the position of the player, in metres
# t, x, and y are arrays

print(x) # example: take a look at x

dt = 0.05 # time increment

# plot the x position and the y position
plt.plot(x,y) # plot the arrays x and y
plt.title('Soccer player x-y position')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()

plt.plot(t,x) # plot the arrays t and x
plt.title('Soccer player x position vs. time')
plt.xlabel('t (s)')
plt.ylabel('x position (m)')
plt.show()


n = len(t) # number of steps: length of t
v_x = np.zeros(n-1) # create an array to store velocity, make 1 element shorter

#### UNCOMMENT FOR PART 1:

for i in np.arange(n-1): # iterate over numbers: i = 0, 1, 2, ... n-2
    v_x[i] = (x[i+1]-x[i])/dt # calculate derivative at i

plt.plot(t[:-1], v_x)
plt.title('Soccer player speed in x direction vs. time')
plt.xlabel('t (s)')
plt.ylabel('v_x (m/s)')
plt.show()

######### PART 1: calculate the velocity in the y-direction

# similar process to calculating velocity in x-direction

v_y = np.zeros(n-1)
# store y velocity values in v_y

for i in np.arange(n-1): # iterate over numbers: i = 0, 1, 2, ... n-2
    v_y[i] = (y[i+1]-y[i])/dt # calculate derivative at i

# uncomment to plot y-velocity
plt.plot(t[:-1], v_y)
plt.title('Soccer player speed in y direction vs. time')
plt.xlabel('t (s)')
plt.ylabel('v_y (m/s)')
plt.show()

#no for loop
vy = (y[:-1]-y[1:])/dt
plt.plot(vy, v_y)
plt.show()


################ UNCOMMENT FOR PART 2

x_int = np.zeros(n) # array to store integrated x value
x_int[0] = x[0] # initial value

for i in np.arange(n-1):
	x_int[i+1] = x_int[i] + v_x[i]*dt

# alternative approach:
x_int_2 = x[0] + np.cumsum(v_x)*dt

plt.plot(t, x_int)
plt.plot(t[:-1],x_int_2)
plt.plot(t,x)
plt.title('Comparison of integrated x-values to original x-values')
plt.show()


################### UNCOMMENT FOR ANIMATION

fig = plt.figure()
ax = plt.axes(xlim=(0,110),ylim=(-5,45))

line1, = ax.plot([],[])
def init():
   line1.set_data([],[])
   return line1,

# define the function that will draw the animation
# for a given value of i, this function will set the data of line1 to have x
# coordinates up to the ith element of x, and y coordinates up to the ith
# element of y
def animate(i):
   line1.set_data(x[:i], y[:i])
   return line1,

numsteps = len(x) # number of steps in the animation


anim = an.FuncAnimation(fig, animate, init_func=init, frames=(numsteps - 1), interval = 1)
# we can add titles and axis labels to animated plots, too
plt.show()