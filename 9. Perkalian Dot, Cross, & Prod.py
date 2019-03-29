import numpy as np

a1 = np.array([1,3,2])
b1 = np.array([3,0,5])

# perkalian dot = hasilnya skalar
# dot = 1*3 + 3*0 + 2*5
c1 = np.dot(a1,b1)
print(c1)

# perkalian cross = hasilnya vektor
a2 = np.array([1,2,0])
b2 = np.array([2,1,0])

c2 = np.cross(a2,b2)
print(c2)
c3 = np.cross(b2,a2)
print(c3)

# perkalian prod
# prod = 1*3*2
c4 = np.prod(a1)
print(c4)
# prod = (1*3) * (3*0) * (2*5)
c5 = np.prod((a1,b1))
print(c5)