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

    # def display(self, node):
    #     # Pre-order traversal to display the tree
    #     result = []
    #     self.ddisplay(self.root, result)
    #     return result
    
    def minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.item

    def maximum(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.item
    
    def search(self, node, key):
        # Base Cases: root is null or key is present at root
        if node is None or node.item == key:
            return node

        # Key is greater than root's key
        if key > node.item:
            return self.search(node.right, key)

        # Key is smaller than root's key
        return self.search(node.left, key)
    
    def delete(self, node, data):
        if node is None:
            return node
        
        if data < node.item:
            node.left = self.delete(node.left, data)

        elif data > node.item:
            node.right = self.delete(node.right, data)
        
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.item = self.minimum(node.right)
            node.right = self.delete(node.right, node.item)
        return node

new_bst = BST()

new_bst.insert(2)
new_bst.insert(3)
new_bst.insert(10)
new_bst.insert(15)
new_bst.insert(6)
new_bst.insert(1)

print(new_bst.display(new_bst.root))  # [3, 5, 10, 15]

# print(new_bst.minimum(new_bst.root))  # 3
# print(new_bst.maximum(new_bst.root))  # 15

# print(new_bst.search(new_bst.root, 88))  # 5
# print(new_bst.search(new_bst.root, 15))  # 5
# print(new_bst.search(new_bst.root, 3))  # 5


new_bst.delete(new_bst.root, 2)
print(new_bst.display(new_bst.root))