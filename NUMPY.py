import numpy as np
print("-"*6, "NUMPY (Numerical Python)", "-"*6)
print("-"*2, "UNSUR-UNSUR NUMPY ARRAY", "-"*2)
# .ndim = dimensi
# .size = elemen
# .shape = ordo 
# print("1. NUMPY ARRAY DIMENSI 1")
# array1 = np.array([1, 2, 3, 4, 5])
# print(f"array1 : {array1}")
# print(f"dimensi : {array1.ndim}")
# print(f"elemen : {array1.size}")
# print(f"ordo : {array1.shape}")
# print(f"array1[2] : {array1[2]}")

# print("2. NUMPY ARRAY DIMENSI 2")
# array2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(f"array2 : {array2}")
# print(f"dimensi : {array2.ndim}")
# print(f"elemen : {array2.size}")
# print(f"ordo : {array2.shape}")
# print(f"array2[0, 1:3] : {array2[0, 1:3]}")
# print(f"array2[0:2, 1:3] : {array2[0:2, 1:3]}")
array = np.array([1, 2, 3, 4, 5, 6])
print(array.reshape(3, 2))




