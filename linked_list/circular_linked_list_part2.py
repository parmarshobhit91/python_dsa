class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class CLL:
    def __init__(self, start = None):
        self.start = start

    def insert_at_start(self):
        value = int(input("Enter the value of the new node : "))
        if self.start == None:
            new_node = Node(value)
            self.start = new_node
            new_node.next = None
            return
        new_node = Node(value)
        new_node.next = self.start
        self.start = new_node
    
    def display(self):
        temp = self.start
        while temp.next.next != None:
            temp = temp.next
        print(temp.data)

    # def display(self):
    #     temp = self.start
    #     while temp != None:
    #         print(temp.data)
    #         temp=temp.next
        

obj = CLL()
obj.insert_at_start()
obj.insert_at_start()
obj.insert_at_start()
obj.insert_at_start()
obj.insert_at_start()
obj.display()
