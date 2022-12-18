import numpy as np

#in a 3x3 grid
Z = np.arange(9).reshape(3,3)


"""
print(Z[[0,1],[0,2]])

would print 0 down 0 right, then 1 down 2 right, rows then columns

"""

print(Z)

#this is how to get the first index
print(Z[0,0])

#how to get last index
print(Z[-1,-1])

#get row
print(Z[1])

#get column
print(Z[:,2])

#get mini-grid (bottom right section), : would just be onwards from that index
print(Z[1:,1:])

#To get the values from corners of a grid and arrange them in a grid format write: Z[::row_size-1,::column_size-1]
print(Z[::2,::2])