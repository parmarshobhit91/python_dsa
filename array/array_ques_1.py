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
print(np.sort(a))

b = np.array([20, 30, 10, 50, 40])
c = sorted(b)
print(c)

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

# largest and smallest without using sort function
largest = a[0]
smallest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
    if a[i] < smallest:
        smallest = a[i]
print(largest)
print(smallest) 

# second largest and second smallest without using sort function
largest = a[0]
second_largest = -999999
smallest = a[0]
second_smallest = 999999
for i in range(len(a)):
    if a[i] > largest:
        second_largest = largest
        largest = a[i]
    elif a[i] > second_largest and a[i] != largest:
        second_largest = a[i]
    if a[i] < smallest:
        second_smallest = smallest
        smallest = a[i]
    elif a[i] < second_smallest and a[i] != smallest:
        second_smallest = a[i]
print(second_largest)
print(second_smallest) 
