class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyCircularLinkedList:
    def __init__(self, start = None):
        self.start = start

    def insert_at_start(self):
        value = int(input("Enter the value of new node : "))
        new_node = Node(value)
        if self.start == None:
            self.start = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return
        new_node.next = self.start
        new_node.prev = self.start.prev
        self.start.prev.next = new_node
        self.start.prev = new_node
        self.start = new_node

    def display(self):
        if self.start is None:
            print("List is empty")
            return
        temp = self.start
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.start:
                break

    # def display(self):
    #     temp = self.start
    #     while temp != self.start.prev:
    #         print(temp.data)
    #         temp = temp.next
    #     print(temp.data)

    def insert_at_end(self):
        value = int(input("Enter the value of new node : "))
        new_node = Node(value)
        if self.start == None:
            self.start = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        new_node.next = self.start
        new_node.prev = self.start.prev
        self.start.prev.next = new_node
        self.start.prev = new_node

    def delete_at_start(self):
        if self.start == None:
            print("List is empty")
            return
        if self.start.next == self.start:
            self.start = None
            return
        self.start.prev.next = self.start.next
        self.start.next.prev = self.start.prev
        self.start = self.start.next

    def delete_at_end(self):
        if self.start is None:
            print("List is empty")
            return
        if self.start.next == self.start:
            self.start = None
            return
        # Remove last node
        self.start.prev.prev.next = self.start
        self.start.prev = self.start.prev.prev

    def insert_at_specific_node(self):
        position = int(input("Enter the value of the node after which you want to insert new node : "))
        value = int(input("Enter the value of the new node : "))
        temp = self.start
        while True:
            temp = temp.next
            if temp.data == position:
                new_node = Node(value)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node
                new_node.next.prev = new_node
                break

    def delete_at_specific_node(self):
        position = int(input("Enter the value of the node which you want to delete : "))
        temp = self.start
        while True:
            temp = temp.next
            if temp.data == position:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                break

# n1 = Node(100)
# n2 = Node(200)
# n3 = Node(300)
# n4 = Node(400)
# n5 = Node(500)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n1

# n5.prev = n4
# n4.prev = n3
# n3.prev = n2
# n2.prev = n1
# n1.prev = n5

# obj1 = DoublyCircularLinkedList(n1)

obj1 = DoublyCircularLinkedList()

# obj1.insert_at_start()
# obj1.insert_at_start()
# obj1.insert_at_start()
# obj1.insert_at_start()

obj1.insert_at_end()
obj1.insert_at_end()
obj1.insert_at_end()
obj1.insert_at_end()
obj1.insert_at_end()

# obj1.insert_at_end()
# obj1.delete_at_start()
# obj1.display()
# print("After deletion")
# obj1.delete_at_end()
# obj1.delete_at_end()
# obj1.delete_at_start()
# obj1.delete_at_start()
obj1.display()

obj1.insert_at_specific_node()
obj1.display()
# obj1.delete_at_end()
print("After delete at end")
obj1.delete_at_specific_node()
obj1.display()