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

def search_bts(root, val):
    if root is None:
        return None 
    
    if root.val == val:
        return root.val
    elif root.val > val:
        return search_bts(root.left, val)
    else:
        return search_bts(root.right, val)
    
def insert_bts(root, val):
    if root is None:
        return Node(val)
    
    if root.val > val:
        root.left = insert_bts(root.left, val)
    else:
        root.right = insert_bts(root.right, val)
    
    return root

def validate_bts(root): 
    if root is None:
        return True
    
    if root.left and root.left.val > root.val:
        return False
    if root.right and root.right.val < root.val:
        return False 
    
    return validate_bts(root.left) and validate_bts(root.right)