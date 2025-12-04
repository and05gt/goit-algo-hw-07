class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def find_min_value(root):
    """Finds the smallest value in a binary search tree."""

    if root is None:
        return None

    current = root

    while current.left is not None:
        current = current.left

    return current.val

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)

print(f"The smallest value in the tree: {find_min_value(root)}")