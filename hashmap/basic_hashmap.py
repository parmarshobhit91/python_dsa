hash_array = [
    [None],
    [None],
    [None],
    [None],
    [None],
    [None],
    [None],
    [None],
    [None],
    [None],
]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10


def add_value(value):
    index = hash_function(value)
    bucket = hash_array[index]
    if value not in bucket:
        bucket.append(value)

def contains_value(value):
    index = hash_function(value)
    bucket = hash_array[index]
    if value in bucket:
        return True
    else:
        return False
    
add_value('shobhit')
print(hash_array)
print("Contains value: ", contains_value('shobhit'), end='\n')

add_value('shivam')
print(hash_array)
print("Contains value: ", contains_value('shivam'))

print(len(hash_array))