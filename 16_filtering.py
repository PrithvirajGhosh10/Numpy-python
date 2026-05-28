import numpy as np
#filtering = refers to the process of selecting elements from  an array that match a given condition
ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])
child= ages[ages<18]
print(child) #[17 16 15]
adults=ages[(ages>=18) & (ages<65) ] # ages in between 18 and 65      op: [21 19 20 30 18 39 22 18 19 20 21]
print(adults)


bacchaburo=ages[(ages<18) | (ages>65) ] # ages not in between 18 and 65      op: [17 16 15 99]
print(bacchaburo)

seniors= ages[ages>=65]
print(seniors) #[65 99]

even=ages[ages%2==0] #[20 16 30 18 22 18 20]
print(even)

odd=ages[ages%2!=0]
print(odd) #[21 17 19 65 39 15 99 19 21]

adults1= np.where(ages>=18,ages,0) #mantain original shape
print(adults1)# [[21  0 19 20  0 30 18 65]
               #[39 22  0 99 18 19 20 21]]