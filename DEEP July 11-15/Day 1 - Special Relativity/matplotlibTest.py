import matplotlib.pyplot as plt
import numpy as np
import math as m

#draw parabola
x = np.arange(-100, 100, 0.1)
y = x**2

plt.plot(x, y)

#visuals:
plt.title("Parabola")
plt.xlabel("x")
plt.ylabel("y")

plt.show()