class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.start = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.start == None:
            self.start = new_node
            new_node.next = None
        new_node.next = self.start
        self.start = new_node
        