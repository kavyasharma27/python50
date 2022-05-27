
import numpy as np


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print("Array : " + str(arr))
n = arr.size
N = 4
M = n//N
resh1 = arr.reshape((N, M))
print("First Reshaped Array : ")
print(resh1)
resh2 = np.reshape(arr, (2, 8))
print("Second Reshaped Array : ")
print(resh2)
