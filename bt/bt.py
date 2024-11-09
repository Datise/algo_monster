from node import Node, NonBNode
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

## Ternary tree

def build_mc_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_mc_tree(nodes, f) for _ in range(num)]
    return NonBNode(f(val), children)

def print_mc_tree(node, level=0):
    # Print the current node with indentation based on its level in the tree
    indent = " " * (level * 4)  # 4 spaces per level of depth for indentation

    print(f"{indent}- {node.val}")

    # Recursively print each child, increasing the level by 1
    for child in node.children:
        print_mc_tree(child, level + 1)

def ternary_tree_paths(root: NonBNode):
    def dfs(root, path, res):
        # exit condition: when a leaf node is reached, append the path to the results
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return


        # DFS on each non-null child
        for child in root.children:
            if child is not None:
                path.append(str(root.val))
                dfs(child, path, res)
                path.pop()
    res = []
    if root: dfs(root, [], res)

    return res