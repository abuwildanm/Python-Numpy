import numpy as np

data = np.array([[11, 22, 33],
		         [44, 55, 66],
		         [77, 88, 99]])

# mengambil kolom ke-0
a = data[:,0]
print(a)

# mengambil semua data dulu, habis itu ambil baris ke-0
# data[:][0] == data[0]
b = data[:][0]
print(b)