import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

aMat = np.zeros((2,3))
bMat = np.ones((2,3))

# stacking matrix, menumpuk matrix

c = np.hstack((a,b))
print("Vector hstack:\n", c) # horizontal
d = np.vstack((a,b))
print("Vector vstack:\n", d) # vertical

cMat = np.hstack((aMat,bMat))
print("Matrix hstack:\n", cMat)
dMat = np.vstack((aMat,bMat))
print("Matrix vstack:\n", dMat)