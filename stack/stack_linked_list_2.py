class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def display(self):
        if self.head == None:
            print("Stack is empty")
            return
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print()

    def pop(self):
        if self.head == None:
            print("Stack is empty")
            return
        self.head = self.head.next
        self.size -= 1

    def stack_size(self):
        print( "Size of stack is: ", self.size)
        return self.size
    
    def is_empty(self):
        if self.head == None:
            print("Stack is empty")
            return True
        print("Stack is not empty")
        return False
    
    def peek(self):
        if self.head == None:
            print("Stack is empty")
            return None
        print("Top element is: ", self.head.data)
        return self.head.data
    
s = Stack()
s.push(10)
s.peek()
s.push(20)
s.peek()
s.push(30)
s.peek()
s.display()
s.stack_size()
s.is_empty()
s.pop()
s.display()
s.pop()
s.peek()
s.display()
s.pop()
s.display()
s.stack_size()
s.is_empty()
s.peek()