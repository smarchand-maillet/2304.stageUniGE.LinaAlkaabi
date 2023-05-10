# from numpy import*
import matplotlib.pyplot as plt
import numpy as np

# fileName = "./data/gaussian-1D-1000-nosep"
fileName = "./data/gaussian-1D-1000-sep"

data= np.genfromtxt(fileName+"-data.csv")
label= np.genfromtxt(fileName+"-label.csv")
#
print("le tableau data a comme taille: {}",data.shape)
print(f"Le tableau label a pour taille: {label.shape}")

#./data/ fais changer de juste stage à la folder data
#c

plt.scatter(label[0], label[1])
plt.show()