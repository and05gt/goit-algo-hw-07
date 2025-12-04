class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def find_max_value(root):
    """Finds the largest value in a binary search tree."""

    if root is None:
        return None

    current = root

    while current.right is not None:
        current = current.right

    return current.val

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(40)

print(f"The largest value in the tree: {find_max_value(root)}")