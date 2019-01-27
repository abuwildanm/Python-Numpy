import numpy as np

print("\n" + 15*"=" + " Vector " + 15*"=")

a = np.floor(np.random.randn(1,6)*10) #array random

print('nilai a:\n',a)

print('nilai max dari a = ',a.max())
print('posisi max dari a = ',a.argmax())
print('nilai min dari a = ',a.min())
print('posisi min dari a = ',a.argmin())

print('mengurutkan nilai a:\n', np.sort(a))
print('mengurutkan indeks nilai a:\n',np.argsort(a))

print("\n" + 15*"=" + " Matrix " + 15*"=")

b = np.floor(np.random.randn(2,2)*10) #array random

print('nilai b:\n',b)

print('nilai max dari b = ',b.max())
print('posisi max dari b = ',b.argmax())
print('nilai min dari b = ',b.min())
print('posisi min dari b = ',b.argmin())

print('mengurutkan nilai b:\n', np.sort(b)) #mengurutkan per baris
print('mengurutkan indeks nilai b:\n',np.argsort(b)) #mengurutkan per baris

print("\n" + 15*"=" + " Multi-Type " + 15*"=")

dtipe = [('nama','S10'),('tinggi',int)]
data = [
	('Ucup',170),
	('Otong', 150),
	('Mario',160)
]

c = np.array(data, dtype = dtipe)
print('nilai c:\n',c)

print('mengurutkan nilai c berdasarkan tinggi:\n', np.sort(c, order='tinggi'))
print('mengurutkan nilai c berdasarkan nama:\n', np.sort(c, order='nama'))