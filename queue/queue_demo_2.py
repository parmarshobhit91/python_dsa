class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.size += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty, Deletion not possible")
            return
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return temp.data 

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next
        print()

    def peek(self):
        return self.front.data
    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def size_of_queue(self):
        return self.size

q = Queue()

print(q.isEmpty())

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.isEmpty())

q.display()

q.dequeue()
print(q.size_of_queue())
print(q.peek())
q.display()

q.dequeue()
q.display()

q.dequeue()
q.display()

q.dequeue()