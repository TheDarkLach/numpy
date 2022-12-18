import numpy as np

#array of 0's
Z = np.zeros(9)
print(Z)

#array of 1's
O = np.ones(9)
print(O)

#for custom array:
C = np.array([1,0,0,0,0,0,0,1,0])
print(C)

#array of 2's, kind weird just take an array of 1's and multiply by 2
T = 2*np.ones(9)
print(T)

#array of size 9, counting up from 0
A = np.arange(9)
print(A)

#reshape an array of 9, 9 rows, 1 column
R = np.arange(9).reshape(9,1)
print(R)

# a 3x3 array of random integers from 0 to 9
R=np.random.randint(0,9,(3,3))
print(R)

#linespace, evenly spaced numbers over the interval 0 to 1, 5 numbers
L = np.linspace(0, 1, 5)
print(L)

#multidemensional meshgrid (array?)
#numbers from 0-3, 3 rows, 3 columns

"""
    ┌───┬───┬───┐   ┌───┬───┬───┐
    │ 0 │ 0 │ 0 │   │ 0 │ 1 │ 2 │
    ├───┼───┼───┤   ├───┼───┼───┤
 M  │ 1 │ 1 │ 1 │   │ 0 │ 1 │ 2 │
    ├───┼───┼───┤   ├───┼───┼───┤
    │ 2 │ 2 │ 2 │   │ 0 │ 1 │ 2 │
    └───┴───┴───┘   └───┴───┴───┘

"""
M=np.mgrid[0:3,0:3]
print(M)