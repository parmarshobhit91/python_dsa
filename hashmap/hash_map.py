class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        char_sum = sum(ord(char) for char in key if not char.isdigit())
        return char_sum % 10
    
    def put(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k,v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
            
    def print_map(self):
        print("Hash Map Data:")
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


s1 = SimpleHashMap(size=10)

s1.put('ab', "Shobhit")
s1.put('abc', "Shrasti")
s1.put('abcd', "Shriyash")
s1.put('abcde', "Shivangi")
s1.put('abcdef', "Utsav")
s1.put('abcdefg', "Vishal")
s1.put('abcdefgh', "Aditya")
s1.put('abcdefghi', "Varnika")

s1.print_map()

print("\nName associated with 'ab'", s1.get("ab"))

print("Updating the name for 'ab' to 'Kinshu'")
s1.put("ab", "Kinshu")

print("Checking if updation success or not for 'ab':", s1.get("ab"))
s1.print_map()

s1.remove("abcdefgh")
print("Removed Aditya")
s1.print_map()