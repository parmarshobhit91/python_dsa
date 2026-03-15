class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        sum_of_char = 0
        for char in value:
            sum_of_char += ord(char)
        return sum_of_char % self.size
    
    def add_value(self, value):
        index = self.hash_function(value=value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains_value(self, value):
        index = self.hash_function(value=value)
        bucket = self.buckets[index]
        return value in bucket
    
    def remove_value(self, value):
        index = self.hash_function(value=value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)
    
    def print_set(self):
        print("Hash Set Data:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

s1 = SimpleHashSet(size=10)
s1.add_value('Shobhit')
s1.add_value('Shrasti')
s1.add_value('Shriyash')
s1.add_value('Shivam')
s1.add_value('Aditya')
s1.add_value('Shivangi')
s1.add_value('Utsav')
s1.add_value('Vishal')

s1.print_set()

print("\n'Shivangi' in the set:", s1.contains_value('shivangi'))
print("Removing 'Shivangi'")
s1.remove_value('Shivangi')
print("'Shivangi' is in the set:", s1.contains_value('Shivangi'))
print("'Shrasti' has hash code:", s1.hash_function('Shrasti'))

print("Contains", s1.contains_value('Dumroo'))