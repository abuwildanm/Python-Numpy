import numpy as np

# membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[3,4,5]), dtype = float)
print("a:\n", a)

# membuat array dengan menggunakan function

def kuadrat(baris,kolom):
	return kolom**2

def jumlah(baris,kolom):
	return (kolom + baris)

# np.fromfunction(fungsi, ukuran matriks, tipe)
b = np.fromfunction(kuadrat, (1,10), dtype = int)
print("b:\n", b)
c = np.fromfunction(jumlah, (4,4), dtype = float)
print("c:\n", c)

# membuat array atau matrix dengan menggunakan iterable

iterable = (x*2 for x in range(5))

d = np.fromiter(iterable, dtype = int)
print("d:\n", d)

# multitype array

dtipe = [('nama','S255'), ('tinggi', int)] # S255 = String dengan max char 255

data = [
	('ucup', 150),
	('otong', 160),
	('mario', 180)
]

e = np.array(data, dtype = dtipe)
print("e:\n", e)