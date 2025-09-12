import numpy as np

a = np.array([10,20,30,40,50])
b = np.array([60,70,80,90,100])

# c = np.concatenate([a,b])
# print(c)

# d = np.concat([a,b])
# print(d)

arr1 = np.array([[10,20,30], [40,50,60]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

res = np.concatenate([arr1, arr2])
# print(res)

# split_res = np.array_split(a,3)
# print(split_res)

# split_res = np.array_split(arr1, 4)
# print(split_res)

# split_res = np.array_split(res,2)
# print(split_res)

# print(np.append(a,200))
# print(np.insert(a,2,500))

# print(np.sum(a))
# print(np.sum(arr1))

# print(np.max(a))
# print(np.min(a))

# print(np.cumsum(a))
# print(np.cumsum(arr1))

# print(np.std(a))
# print(np.var(a))

print(np.__version__)