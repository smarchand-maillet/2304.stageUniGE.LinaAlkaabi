import numpy as np
import matplotlib.pyplot as plt
from turtle import*

box = np.genfromtxt("gaussian-2D-1000-nosep-data.csv", delimiter=',')

def box2(box):
    x_gauche = min(point[0] for point in box)
    y_gauche = min(point[1] for point in box)
    x_droite = max(point[0] for point in box)
    y_droite = max(point[1] for point in box)

    return [(x_gauche, y_gauche), (x_droite, y_droite)]

plt.plot(box2(box), color='red')
box2(box)
med= np.median(box)
print(med)
plt.plot(med,med, color='blue')
plt.show()

gaussian-2D-1000-nosep-data.csv


med= np.median(box)
plt.plot(med,med, color='blue')
plt.show()

