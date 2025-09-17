class Node: 
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self, last = None):
        self.last = last
    
    def display(self):
        temp = self.last.next
        while temp != self.last:
            print(temp.data)
            temp = temp.next
        print(temp.data)

    
    def insert_at_first(self, data):
        if self.last == None:
            new_node = Node(data)
            self.last = new_node
            new_node.next = new_node
            return
        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node

    def insert_at_end(self, data):
        if self.last == None:
            new_node = Node(data)
            self.last = new_node
            return
        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    def delete_at_first(self):
        if self.last == None:
            print("List is empty")
            return
        if self.last.next == self.last:
            self.last = None
            return
        self.last.next = self.last.next.next

    def delete_at_last(self):
        if self.last == None:
            print("List is empty")
            return
        if self.last.next == self.last:
            self.last = None
            return
        temp = self.last.next
        while temp.next != self.last:
            temp = temp.next
        temp.next = self.last.next
        self.last = temp

    def insert_at_specific_position(self):
        position = int(input("Enter the value of node after which you want to insert the new node : "))
        data = int(input("Enter the data of new node : "))
        temp = self.last
        while temp.data != position:
            temp = temp.next
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # def delete_at_specific_position(self):
    #     position = int(input("Enter the value of node which you want to delete : "))
    #     temp = self.last
    #     while temp.next.data != position:
    #         temp = temp.next
    #     temp.next = temp.next.next

    def delete_at_specific_position(self):
        position = int(input("Enter the value of node which you want to delete : "))
        temp = self.last
        while temp.next.next != None:
            if temp.next.data == position:
                temp.next = temp.next.next
                return
            temp = temp.next
n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n1

k = CircularLinkedList(n4)

# k = CircularLinkedList()

# k.insert_at_first(100)  
# k.insert_at_first(200)  
# k.insert_at_first(300)  
# k.insert_at_first(400)  
k.display()
# k.insert_at_end(4545)
# k.insert_at_end(6767)
# k.delete_at_first()
# k.delete_at_last()
# k.insert_at_specific_position()
# k.delete_at_specific_position()
# k.delete_at_last()
k.delete_at_specific_position()
print("After deletion")
k.display()