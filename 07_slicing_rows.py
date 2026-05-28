import numpy as np
array=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])


#     array[start:end:step]

# print(array[1])  #[5 6 7 8]
# print(array[-1]) #[13 14 15 16]
print(array[1:])#[[ 5  6  7  8]
                 #[ 9 10 11 12]
                #[13 14 15 16]]
print(array[0:4:])# print first 4 rows

print(array[0:4:2])#print row first and third , skip between rows
print(array[::2])#same

print(array[::-1])#from bottom to top


print(array[::-2]) #from bottom to top,skip between rows
