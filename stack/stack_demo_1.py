class Stack:
    def __init__(self):
        self.stack = []

    def push(self):
        element = int(input("Enter the value of the element you want to insert : "))
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def display(self):
        print(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
s = Stack()
print(s.isEmpty())
s.push()
s.push()
s.push()

s.display()
print("Size of stack : ", s.size())
s.pop()

print("After pop")
s.display()

print("Peek element : ", s.peek())
print("Size of stack : ", s.size())