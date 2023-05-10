from numpy import random
import numpy as np
prune_cerise = np.random.randint(40, size=(10))
l=[]
for i in prune_cerise:
    if i>=18:
       l.append(0)
    else:
        l.append(1)
print(l)
prune_cerise1 = np.random.randint(10, size=(10))
l2=[]
for i in prune_cerise1:
    if i>=4:
        l2.append(0)
    else:
        l2.append(1)
print(l2)


data=np.zeros((40,2))
l=[]
diam_cerise = np.random.randn(10, size=(10))+2
for i in range(10):
    l.append(0)
diam_prune= np.random.randn(10, size=(10))+6
for i in range(10):
    l.append(1)
poids_cer=np.random.randn(10, size=(10))+30
for i in range(10):
    l.append(0)
poids_prune = np.random.randn(10)+5
for i in range(10):
    l.append(1)

savetxt("data1.csv", data1, delimiter=",")

