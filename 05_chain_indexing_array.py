# chain indexing
import numpy as np
a=np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
            [['j','k','l'],['m','n','o'],['p','q','r']],
            [['s','t','u'],['v','w','x'],['y','z',' ']]]) # 3 dimentional array
print(a[0][0][0]) #op: a

# multidimensional indexing
print(a[0,0,0]) #a
print(a[0,0,1]) #b
print(a[0,0,2]) #c
# print(a[0,0,3]) #a print(a[0,0,3]) #a IndexError: index 3 is out of bounds for axis 2 with size 3
#so
print(a[0,1,0]) #d
print(a[0,1,1]) #e
print(a[1,1,1]) #n
print(a[2,2,2]) # ' '
