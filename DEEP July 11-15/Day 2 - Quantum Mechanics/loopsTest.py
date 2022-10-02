import numpy as np

n = 10
r = np.zeros(n)
r[0] = 4

for i in np.arange(n-1):
    r[i+1] = r[i]+4


print(r)