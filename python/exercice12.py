import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("gaussian-2D-1000-sep-data.csv")
labels = pd.read_csv("gaussian-2D-1000-sep-label.csv")

#pr séparer tabl en 2 colonnes
X, y = data.values, labels.values.ravel()
random_index = np.random.randint(len(X))
random_data = X[random_index]
k = 5
distances = np.sqrt(np.sum(np.square(X - random_data), axis=1))
k_neighbors_labels = y[distances.argsort()[:k]]

# occurence k + proche
label_predic = np.bincount(k_neighbors_labels).argmax()

print("Label connu: ", y[random_index])
print("Label prédit: ", label_predic)

plt.scatter(X[:, 0], X[:, 1], c="black", alpha=0.1)
plt.scatter(random_data[0], random_data[1], c='red', marker='s', label='Donnée aléatoire')
plt.scatter(X[distances.argsort()[:k], 0], X[distances.argsort()[:k], 1], c='green', marker='o', label='K plus proches voisins')
plt.legend()
plt.show()
