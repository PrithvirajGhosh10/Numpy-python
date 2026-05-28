import numpy as np
array=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])
print(array[:,0]) #print first column #op: [ 1  5  9 13]
# : must be there to represent rows otherwise it will show error
print(array[:,1]) #2nd column
print(array[:,-1]) #last column

#range
print(array[:,0:3])#print first 3 column
print(array[:,::2])##print columns first and third , skip between columns
print(array[:,::-1])#print from last cloumn to first