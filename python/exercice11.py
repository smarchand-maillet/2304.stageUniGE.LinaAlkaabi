import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("gaussian-2D-1000-sep-data.csv")

#iloc: donne ou remplace valeurs 
X, y = data.iloc[:, :-1].values, data.iloc[:, -1].values

# distance
donne = X[np.random.randint(len(X))]
distances = np.sqrt(np.sum(np.square(X - donne), axis=1))
k=5
k_plus_proches = distances.argsort()[:k]
print("Le chiffre était", donne)
print("Les étiquettes des {} plus proches voisins:".format(k))
print(y[k_plus_proches])

plt.scatter(X[:,0], np.zeros_like(X[:,0]), c="k", alpha=0.1)
plt.scatter(donne[0], 0, c='r', marker='s', label='donnée random')
plt.scatter(X[k_plus_proches, 0], np.zeros_like(X)[k_plus_proches], c='g', marker='o', label='k-plus proches')
plt.legend()
plt.show()
