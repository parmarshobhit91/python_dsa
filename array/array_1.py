import numpy as np

# BASIC ARRAY OPERATIONS AND TYPES OF ARRAYS
# 1D ARRAY
# 2D ARRAY
# shape, len, type, indexing, slicing
# add, subtract, multiply, divide, mod, power



a = np.array([1, 2, 3, 4, 5])
# print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)

# print(a[1:4])
# print(b[0, 0:3])
# print(b[0:1, 0:3])

# print(b.shape)
# print(len(b))
# print(type(b))
# print(type(a))
# print(len(a))

array_1 = np.array([1, 2, 3, 4])
array_2 = np.array([5, 6, 7, 8])

sum_array = array_1 + array_2
array_sum = np.add(array_1, array_2)
print(sum_array)  

diff_array = array_1 - array_2
array_diff = np.subtract(array_1, array_2)
print(diff_array)

prod_array = array_1 * array_2
array_prod = np.multiply(array_1, array_2)
print(prod_array)

div_array = array_1 / array_2
array_div = np.divide(array_1, array_2)
print(div_array)

mod_array = array_1 % array_2
array_mod = np.mod(array_1, array_2)
print(mod_array)

pow_array = array_1 ** 2
array_pow = np.power(array_1, 2)
print(pow_array)