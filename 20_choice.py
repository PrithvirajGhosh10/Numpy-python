import numpy as np
rng=np.random.default_rng()
fruits=np.array(["🍎","🍊","🍌","🥥","🍍"]) #for emojies - press - window + ;
# fruits=rng.choice(fruits)
# print(fruits)

# fruits=rng.choice(fruits,size=3)# with size of choosing
# print(fruits)

fruits=rng.choice(fruits,size=(3,3))# with size of choosing #2d
print(fruits)