class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class SinglyLinkedList:
    def __init__(self,start = None):
        self.start = start

    # Linked List is empty or not (True/False) defining is_empty method
    def is_empty(self):
        return self.start == None    # True if self.start is None else False 
    
    # Defining add_at_start method
    def add_at_start(self, item):
        new_node = Node(item, self.start)
        self.start = new_node

    # Defining display method
    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next

    # Defining add_at_end method
    def add_at_end(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.start = new_node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    # Defining delete_at_start method
    def delete_at_start(self):
        if self.is_empty():
            print("Linked List is empty, deletion not possible")
            return
        self.start = self.start.next

    # Defining search element in list method
    def search(self,value):
        temp = self.start
        while temp != None:
            if value == temp.item:
                print("Element found")
                return
            temp = temp.next
        print("element not found")

    # Defining delete_at_end method
    def delete_at_end(self):
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    # Defining insert_at_any_point method
    def insert_at_any_index(self):
        temp = self.start
        value = int(input("Enter a value after which you want to insert a node : "))
        data = int(input("Enter the data for the new node : "))
        new_node = Node(data)
        while temp != None:
            if temp.item == value:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
    
    # Defining delete_at_any_index method
    def delete_at_any_index(self):
        temp = self.start
        value = int(input("Enter the value of the node you want to delete : "))
        while temp.next != None: 
            if temp.next.item == value:
                temp.next = temp.next.next
                return
            temp = temp.next

   
# Creating Nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

# Linking nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None

# Creating Singly Linked List object
sll = SinglyLinkedList(n1)

# Checking if linked list is empty or not
# print(sll.is_empty())

# Adding element at start of linked list
# sll.add_at_start(500)

# Displaying linked list elements
# sll.display()

# Adding element at end of linked list
# sll.add_at_end(1000)

# print("After adding element at end:")
# sll.display()



# sll.display()
# print(n1.item)
# print(n1.next)

# print(n1.next.next.item)
# print(n1.next.next.item)

# print(n2.item)

# print(n1.next.item == n2.item)

# sll.search(20)

sll.display()
# sll.insert_at_any_index()
sll.delete_at_any_index()
sll.display()