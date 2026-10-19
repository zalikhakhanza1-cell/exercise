import numpy as np
print("-" * 5, "LEARN NUMPY", "-" * 5)

# ARRAY DIMENSIONS
print("ARRAY DIMENSIONS:")
# .ndim = dimensi
# .shape = ukuran
# .size = jumalah elemen
print("1. 1D array")
array_1d = np.array([1, 2, 3])
dimensions = array_1d.ndim
size = array_1d.shape
elemen = array_1d.size
print(f"array 1d: {array_1d}")
print(f"dimensi: {dimensions}")
print(f"ukuran: {size}")
print(f"jumlah elemen: {elemen}")
print("2. 2D array")
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
dimensions = array_2d.ndim
size = array_2d.shape
elemen = array_2d.size
print(f"array_2d: {array_2d}")
print(f"dimensi: {dimensions}")
print(f"ukuran: {size}")
print(f"jumalah elemen: {elemen}")
print("3. 3D array")
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
dimensions = array_3d.ndim
size = array_3d.shape
elemen = array_3d.size
print(f"array_3d: {array_3d}")
print(f"dimensi: {dimensions}")
print(f"size: {size}")
print(f"jumlah elemen: {elemen}")
