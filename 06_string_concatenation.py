#form a three letter word using string concatenation. 
import numpy as np
a=np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
            [['j','k','l'],['m','n','o'],['p','q','r']],
            [['s','t','u'],['v','w','x'],['y','z',' ']]])
#peaking letter (a,s)
word= a[0,0,0]+ a[2,0,0]+a[2,0,0]
print(word) #op:ass
