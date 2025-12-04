class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def get_sum_iterative(root):
    """Iteratively finds the sum of all values (using the stack)."""

    if root is None:
        return 0
    
    total_sum = 0
    stack = [root]

    while stack:
        current_node = stack.pop()
        total_sum += current_node.val

        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)

    return total_sum

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(40)

print(f"Sum of all values: {get_sum_iterative(root)}")