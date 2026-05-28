import numpy as np 
#floating point no
np.random.seed(seed=1)#reproduce the same no.
print(np.random.uniform()) #op:0.8521259267238278
print(np.random.uniform(low=-1,high=1)) #-0.2436032004385793
print(np.random.uniform(low=-1,high=1,size=(3,2))) # 2d array
'''
[[ 0.99711888  0.37809234]
 [ 0.7567338   0.39885771]
 [-0.26218327  0.06124328]]

'''
