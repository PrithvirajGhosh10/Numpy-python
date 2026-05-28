import numpy as np
#vectorized math functions #1d list
b=np.array([1,2,3])
print(np.sqrt(b)) #op:[1.         1.41421356 1.73205081] #numpy have some buildin function in it
c=np.array([1.01,2.33,4.321])
print(np.round(c)) #op:[1. 2. 4.]
print(np.floor(c))#op: [1. 2. 4.]
print(np.ceil(c))#op: [2. 3. 5.]
print(np.pi)#3.141592653589793


#exercise:circle
radius=np.array([1,2,3,])
print(np.pi*radius**2)#op:[ 3.14159265 12.56637061 28.27433388] #formula: area=pi r^2


radiii=int(input("Enter radius of circle: "))
print("Area of the circle is: ",np.pi*radiii**2)