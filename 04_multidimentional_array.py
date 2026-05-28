import numpy as np
array=np.array('a') #0 dimentional array
print(array.ndim) #no. of dimentions

a=np.array(['a','b','c'])#1 dimentional array
print(a.ndim)
print(a.shape) #(3,)

b=np.array([['a','b','c'],
            ['d','e','f'],
            ['g','h','i']]) #2 dimentional array
print(b.ndim)
print(b.shape)#(3, 3)

c=np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
            [['j','k','l'],['m','n','o'],['p','q','r']],
            [['s','t','u'],['v','w','x'],['y','z',' ']]]) # 3 dimentional array
print(c.ndim)
print(c.shape) #(3, 3, 3) # 3 layers,3 rows , 3 calumns

d=np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
            [['j','k','l'],['m','n','o'],['p','q','r']]]) # 3 dimentional array
print(d.ndim)
print(d.shape) #(2, 3, 3) # 2 layers,3 rows , 3 calumns




