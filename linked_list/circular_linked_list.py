class Node: 
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self, last = None):
        self.last = last
    
    def insert_at_first(self, data):
        new_node = Node(4000)
        new_node.next = self.last.next
        self.last.next = new_node


n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)

n1.next = n2
n2.next = n3
n3.next = n4

k = CircularLinkedList(n4)
k.insert_at_first(100)