class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class Queue:
    def __init__(self):
        self.front = None
        self.size = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.front == None:
            self.front = new_node
            self.size += 1
            return
        temp = self.front
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        self.size += 1

    def dequeue(self):
        if self.front == None:
            print("Queue is empty, Deletion not possible")
            return
        self.front = self.front.next
        self.size -= 1

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next
        print()

    def peek(self):
        return self.front.data
    
    def isEmpty(self):
        if self.front == None:
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