import numpy as np  
import matplotlib.pyplot as plt   
from random import randint

levels=int(input("How many levels do you want?(min 1) ") or 10)
x=np.arange(0,levels+1) 
if levels>=1:
    rails=[0]*(levels+1)
else:
    print("The value of levels can't be lower than 1.")
    exit()

for h in range(0,(levels+1)**2*100):
    stored=0
    for j in range(0,levels):
        stored+=randint(0,1)
    rails[stored]+=1
print(rails)