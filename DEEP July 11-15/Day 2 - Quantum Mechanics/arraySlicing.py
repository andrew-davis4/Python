# array slicing

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(20) 
# a is a numpy array created using the arange function from the numpy
# module
print(a) # print how a looks; a range from 0 up to but not including 20

# what if we only want part of a? between the 2nd (counting from 0) and 
# up to but not including the 10th element

print(a[2:10]) # takes a subset of the array

# the colon represents taking a range of indices; indices from 2 to 10

# tip: you can get the length of an array using the len() function

print(len(a))
print(len(a[2:10]))


# arrays can also be sliced from just the beginning or just the end, and
# you can also use negative indices

# here's some examples

print(a[:5])
print(a[2:-2])
print(a[:-1])

# you can also take every 2nd or 3rd or nth element of an array with a slicing
# argument. 
# for every other element:

print(a[::2])

# to step through a backwards:

print(a[::-1])

# you can also combine this with other slicing operations
print(a[1::3])
print(a[2:18:2])


plt.plot(a[1:], a[:-1])
plt.show()