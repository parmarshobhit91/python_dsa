import numpy as np

# Check numpy version
# print(np.__version__)

# Creating arrays
a = np.array([10,20,30,40,50])
b = np.array([60,70,80,90,100])

# concatenation of arrays (1D arrays)
# c = np.concatenate([a,b])
# print(c)

# d = np.concat([a,b])
# print(d)

# Creating 2D arrays
arr1 = np.array([[10,20,30], [40,50,60]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Concatenation of 2D arrays
# a = np.concatenate([arr1, arr2], axis=0)  # vertical stacking
# print(a)
# a = np.concatenate([arr1, arr2], axis=1)  # horizontal stacking
# print(a)
# res = np.concatenate([arr1, arr2])
# print(res)

# Splitting arrays
# split_res = np.array_split(a,3)
# print(split_res)

# split_res = np.array_split(arr1, 4)
# print(split_res)

# split_res = np.array_split(res,2)
# print(split_res)

# append and insert method for 1D arrays
# print(np.append(a,200))
# print(np.insert(a,2,500))

# append and insert method for 2D arrays
# print(np.append(arr1, [[70,80,90]], axis=0))
# print(np.append(arr2, [[70],[80]], axis=1))

# print(np.insert(arr1, 1, [15,25,35], axis=0))
# print(np.insert(arr2, 1, [15,25], axis=1))

# Sum of elements, max, min, cumsum, std, variance, cumprod
# print(np.sum(a))
# print(np.sum(arr1))

# print(np.max(a))
# print(np.max(arr1))
# print(np.min(a))
# print(np.min(arr1))

# print(np.cumsum(a))
# print(np.cumsum(arr1))

# print(np.cumprod(a))
# print(np.cumprod(arr1))

# print(np.std(a))
# print(np.var(a))
