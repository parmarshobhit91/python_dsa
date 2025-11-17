# Arranging data in some logical order is called sorting.
# Sorting can be done in ascending or descending order.
# Sorting we are going to cover is also known as internal sorting,
# When elements are numbers arranging them in ascending order means sorting.
# When elements are strings arranging them in lexicographical/dictionary/alphabetical order means sorting.

# Bubble Sort
# Modified Bubble Sort

# 22 , 21 , 19 , 18 , 45 , 23
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
# arr = [22, 21, 19, 18, 45, 23]
# print(bubble_sort(arr))  # Output: [18, 19, 21, 22, 23, 45]

# 22, 21 , 19 , 18 , 45 , 23
def modified_bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        count += 1
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, count
arr = [22, 21, 19, 18, 45, 23]
print(modified_bubble_sort(arr))  # Output: ([18, 19, 21, 22, 23, 45], 4)