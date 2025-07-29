class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example binary tree
root = BinaryNode(1)
root.left = BinaryNode(2)
root.right = BinaryNode(3)
