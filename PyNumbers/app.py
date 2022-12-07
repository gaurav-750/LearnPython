import numpy as np


arr = np.array([[1, 2, 3], [4, 5, 6]])
print(type(arr))
print(arr)
print(arr.shape)

arr2 = np.zeros((3, 4), dtype=int)
print(arr2)

arr3 = np.full((2, 3), 9, dtype=int)
print(arr3)


arr4 = np.random.random((3, 3))
print(arr4)
