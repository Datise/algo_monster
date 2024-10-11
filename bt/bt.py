from nodes import Node
def build_tree(nodes, f):
    try:
        val = next(nodes)
    except StopIteration:
        return None
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)