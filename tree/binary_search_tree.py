class Node:
    def __init__(self, item = None, right = None, left = None):
        self.item = item
        self.right = right
        self.left = left

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.iinsert(self.root, data)

    def iinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.iinsert(root.left, data)
        else:
            root.right = self.iinsert(root.right, data)
        return root

    # def insert(self, item):
    #     # If tree is empty, create the root node
    #     if self.root is None:
    #         self.root = Node(item)
    #         return

    #     # Otherwise, find the correct position
    #     current = self.root
    #     while True:
    #         if item < current.item:
    #             # Go left
    #             if current.left is None:
    #                 current.left = Node(item)
    #                 break
    #             else:
    #                 current = current.left
    #         elif item > current.item:
    #             # Go right
    #             if current.right is None:
    #                 current.right = Node(item)
    #                 break
    #             else:
    #                 current = current.right
    #         else:
    #             # If item already exists (optional: skip or handle duplicates)
    #             break

    def display(self, node):
        # In-order traversal to display the tree
        result = []
        self.ddisplay(self.root, result)
        return result
    
    def ddisplay(self, root, result):
        if root != None:
            self.ddisplay(root.left, result)
            result.append(root.item)
            self.ddisplay(root.right, result)


new_bst = BST()

new_bst.insert(10)
new_bst.insert(5)
new_bst.insert(15)
new_bst.insert(3)

print(new_bst.display(new_bst.root))  # [3, 5, 10, 15]