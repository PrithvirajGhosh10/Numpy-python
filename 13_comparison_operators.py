import numpy as np
#comparison operators
score=np.array([91,55,67,86,100])
print(score==100) #any of the score is equal to 100        op:[False False False False  True]
print(score>=70) #score above 70                           op:[ True False False  True  True]
print(score<=70) #score less than 70                       op:[False  True  True False False]
score[score<70]=0
print(score)     #marks <70 will be 0                      op:[ 91   0   0  86 100]
