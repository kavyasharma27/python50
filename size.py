
import numpy as np


x = np.array([100,20,34])

print("Size of the array: ",
	x.size)

print("Memory size of one array element in bytes: ",
	x.itemsize)

# memory size of numpy array in bytes
print("Memory size of numpy array in bytes:",
	x.size * x.itemsize)
