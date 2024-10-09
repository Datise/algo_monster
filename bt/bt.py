class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)