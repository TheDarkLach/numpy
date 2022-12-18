"""The term broadcasting describes how numpy treats arrays with different shapes during arithmetic operations. Subject to certain 
constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes. 
Broadcasting provides a means of vectorizing array operations."""
import numpy as np

Z1 = np.arange(9).reshape(3,3)
print(Z1)
Z2 = 1
#adds 1 to each index
print(Z1 + Z2)

Z1 = np.arange(9).reshape(3,3)
Z2 = np.arange(3)[::-1].reshape(3,1)

#adds 2 1 0 down the first column
print(Z1 + Z2)

Z1 = np.arange(9).reshape(3,3)
Z2 = np.arange(3)[::-1]

#same thign as before but adds it to first row
print(Z1 + Z2)