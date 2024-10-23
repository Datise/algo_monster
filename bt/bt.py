from node import Node
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

def print_tree(node, level=0):
    if level == 0:
        print("\n")
    if node != None:
        print_tree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        print_tree(node.right, level + 1)