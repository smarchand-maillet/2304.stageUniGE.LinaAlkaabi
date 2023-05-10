import numpy as np

donnees= np.genfromtxt("../../data/gaussian-2D-1000-nosep-data.csv", delimiter=",")
moy = np.mean(donnees)
print(moy)
variance = np.std(donnees)
variance

import pandas as pd
data_row = data[data.x2 < 20]                              # Remove particular rows
print(data_row)

