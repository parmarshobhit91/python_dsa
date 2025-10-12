class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)
    
    def dequeue(self):
        if len(self.items) == 0:
            print("Unable to Dequeue! Queue is empty")
            return
        temp = list[0]
        self.items.pop(0)
        return temp
    
    def display(self):
        if len(self.items) == 0:
            print("Queue is empty")
            return
        print(self.items)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size_of_queue(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
q = Queue()

q.enqueue(10)
q.enqueue(20)

print(q.peek())

q.enqueue(30)

print(q.isEmpty())
print(q.size_of_queue())

q.display()

q.dequeue()
q.display()

print(q.peek())

q.dequeue()
q.display()

q.dequeue()
q.display()

q.dequeue()

print(q.isEmpty())
print(q.size_of_queue())