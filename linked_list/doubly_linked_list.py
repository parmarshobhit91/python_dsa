class Node:
    def __init__(self, data = None, prev = None , next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
    def __init__(self, start = None):
        self.start = start

    def insert_at_start(self):
        value = int(input("Enter value of new node : "))
        new_node = Node(value)
        new_node.next = self.start
        new_node.prev = None
        if self.start is not None:
            self.start.prev = new_node
        self.start = new_node

    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def insert_at_end(self):
        temp = self.start
        value = int(input("Enter the value of the node :"))
        new_node = Node(value)
        if self.start == None:
            self.start = new_node
            return
        while temp.next != None:
            temp = temp.next
        new_node.prev = temp
        temp.next = new_node
        
    def delete_at_start(self):
        if self.start == None:
            print("List is empty.")
            return
        self.start = self.start.next
        self.start.next.prev = None

    def delete_at_end(self):
        if self.start == None:
            print("List is empty.")
            return
        temp = self.start.next
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def search(self):
        temp = self.start
        value = int(input("Enter a value you want to search in the list : "))
        while temp != None:
            if temp.data == value:
                print("Element exits")
                return
            temp = temp.next
        print("Element does not exist")


n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)
n5 = Node(500)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None

n1.prev = None
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4

obj1 = DLL(n1)

# print(n4.prev.data)
# print(n1.next.data)

# obj1.insert_at_start()

# print(obj1.start.data)

# obj1.insert_at_end()

# obj1.delete_at_start()
# obj1.delete_at_end()
obj1.search()
# obj1.display()