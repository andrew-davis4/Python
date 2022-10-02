import numpy as np
import matplotlib.pyplot  as plt

x = np.linspace(0, 2*np.pi, 1000)
print(x)
h = np.pi # what happens when you change this value?
y1 = np.sin(x) # sine
y2 = np.sin(x-h) # sine with horizontal shift

s = y1 + y2 # sum of sines

# create plots
# the arguments '--' and '-.' define different line shapes
# the label argument defines labels for the legend (strings)
plt.plot(x, y1, '--', label='y1 = sin(x)') 
plt.plot(x, y2, '-.', label='y2 = sin(x+h)')

plt.plot(x, s, label='y1 + y2')

plt.title('Sum of sines') # function which creates plot title (string)
plt.xlabel('Angle (radians)') # function which labels x axis of plot
plt.ylabel('Amplitude') # function which labels y axis 

plt.legend() # show the legend
plt.show()