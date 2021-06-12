import numpy as np
import matplotlib.pyplot as plt
from random import randint

levels = int(input("How many levels do you want?(min 1/ 20 by default) ") or 20)

if levels >= 1:
    lanes = [0]*(levels)
else:
    print("The value of levels can't be lower than 1.")
    exit()

for h in range((levels)**2*100):
    stored = -1
    for j in range(levels):
        stored += randint(0, 1)
    lanes[stored] += 1
print((levels)**2*100, "balls were used in totall")
print(lanes)

X = np.arange(-((len(lanes)/2)-.5), (len(lanes)/2)+.5)
plt.suptitle('Galton Board')
plt.bar(X + 0.00, lanes, width=0.25)
plt.show()
