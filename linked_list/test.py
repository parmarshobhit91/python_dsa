class Node:
    def __init__(self, data = None , next = None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self, start = None):
        self.start = start
        
    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
    def is_empty(self):
        return self.start == None 
        
    def delete_at_start(self):
        if self.is_empty():
            print("Linked List is empty, deletion not possible")
            return
        self.start = self.start.next
        
    # defineing delete_at_end method
    def delete_at_end(self):
        # if self.is_empty():
        #     print("Linked List is empty, deletion not possible")
        #     return
        # if self.start.next is None:
        #     self.start = None
        #     return
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


        
    def add_at_end(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.start = new_node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
# obj1.display()
# obj1.delete_at_start()
# obj1.display()

obj1 = SLL()
obj1.add_at_end(10)
obj1.add_at_end(20)
obj1.add_at_end(30)
obj1.add_at_end(40)

obj1.display()
print("after deletion")
obj1.delete_at_end()
obj1.display()
