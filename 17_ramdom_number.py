import numpy as np
# randon number gerarator          #rng()
a=np.random.default_rng()
# a=np.random.default_rng(seed=1)  #same
print(a.integers(low=1,high=7)) #1-6
print(a.integers(low=1,high=101,size=3 )) #1-100 
#size= no of elements to choose
print(a.integers(low=1,high=101,size=(3,2) ))#for 2d array