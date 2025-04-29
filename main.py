class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert(current_node.right, value)

    # Inorder Traversal
    def inorder_traversal(self, current_node):
        if current_node:
            self.inorder_traversal(current_node.left)
            print(current_node.value, end=" ")
            self.inorder_traversal(current_node.right)

    def preorder_traversal(self, current_node):
        if current_node:
            print(current_node.value, end=" ")
            self.preorder_traversal(current_node.left)
            self.preorder_traversal(current_node.right)

    def postorder_traversal(self, current_node):
        if current_node:
            self.postorder_traversal(current_node.left)
            self.postorder_traversal(current_node.right)
            print(current_node.value, end=" ")



# Creates binary tree with root node = 27
tree = BinaryTree(27)

values_to_insert = [14, 35, 31, 10, 9]
for value in values_to_insert:
    tree.insert(tree.root, value)

#          27
#        /    \
#      14      35
#     /       /
#    10      31
#   /
#  9

print("\nTree elements in sorted order: ")
tree.inorder_traversal(tree.root) # 9 10 14 27 31 35

print("\nTree elements in preorder: ")
tree.preorder_traversal(tree.root) # 27 14 10 9 35 31


print("\nTree elements in post order: ")
tree.postorder_traversal(tree.root) # 9 10 14 31 35 27

# Level order traversal -> 27 14 35 10 31 9