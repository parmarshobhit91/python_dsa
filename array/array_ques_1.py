import numpy as np

# create a 1D array
a = np.array([1, 2, 3, 4, 5])
print(a)

# reverse the array
print(a[::-1])

# maximum value in the array
print(np.max(a))

# minimum value in the array
print(np.min(a))

# product of max and min
print(np.max(a) * np.min(a))

# sum of max and min
print(np.max(a) + np.min(a))

# sort the array
# print(np.sort(a))

# sort the array without using inbuilt function
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            # a[i], a[j] = a[j], a[i]
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)

# second smallest and second largest using sort function
sort_array = np.sort(a)
print(sort_array[1])
print(sort_array[-2])

# min
temp = a[0]
for i in range(len(a)):
    if a[i] < temp:
        temp = a[i]
print(temp)

# max
temp = a[0]
for i in range(len(a)):
    if a[i] > temp:
        temp = a[i]
print(temp)

# sort without using inbuilt function
array_1 = np.array([1, 0, 0, 1, 0, 1])
for i in range(len(array_1)):
    for j in range(i + 1, len(array_1)):
        if array_1[i] > array_1[j]:
            temp = array_1[i]
            array_1[i] = array_1[j]
            array_1[j] = temp
print(array_1)