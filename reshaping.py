import numpy as np

#pretty simple


#base
Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0])
print(Z)

#basic reshaping Z=np.array(1D_array).reshape(x_dimension,y_dimension)

#12 rows, 1 column
Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0]).reshape(12,1)
print(Z)

#3 rows 4 columns
Z = np.array([0,0,0,0,0,0,0,0,0,0,1,0]).reshape(3,4)
print(Z)