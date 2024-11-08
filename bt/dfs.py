# global var for educational purposes to show
# different return strategies
import pdb
from node import Node

global_found = None
class DFS:

    # search using global variable strategy
    def search_global(self, node, target):
        global global_found
        if node is None:
            return None

        if node.val == target:
            global_found = node
            return

        self.search_global(node.left, target)
        self.search_global(node.right, target)

        return global_found

    # search using return + divide and conquer strategy
    def search(self, node, target):
        if node is None:
            return None

        if node.val == target:
            return node

        found = self.search(node.left, target)
        return found if found else self.search(node.right, target)

    def find_highest_val(self, node) -> int:
        if node is None:
            return 0

        left_highest = self.find_highest_val(node.left)
        right_highest = self.find_highest_val(node.right)
        return max(node.val, left_highest, right_highest)

    def find_max_depth(self, root) -> int:
        def max_depth(root):
            if not root:
                return 0
            return max(max_depth(root.left), max_depth(root.right)) + 1

        return max_depth(root) - 1 if root else 0

    def visible_tree_nodes(self, root):
        def visible(node, max_so_far):
            if node is None:
                return 0

            total = 0
            if node.val > max_so_far:
                total += 1

            total += visible(node.left, max(max_so_far, node.val))
            total += visible(node.right, max(max_so_far, node.val))

            return total

        return visible(root, -1)

    def is_balanced(self, root):
        def check(left, right):
            return left - right <= 1 and left - right >= -1

        def balanced(node):
            if node is None:
                return 0

            return max(balanced(node.left), balanced(node.right)) + 1

        left = balanced(root.left)
        right = balanced(root.right)
        return check(left, right)

    def is_same_tree(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None or tree2 is None:
            return False
        
        return tree1.val == tree2.val and self.is_same_tree(tree1.left, tree2.left) and self.is_same_tree(tree1.right, tree2.right)
        


    def sub_tree_of_another_tree(self, root, subroot):
        if root is None:
            return False

        if self.is_same_tree(root, subroot):
            return True
        
        return self.sub_tree_of_another_tree(root.left, subroot) or self.sub_tree_of_another_tree(root.right, subroot)

    def invert_tree(self, root):
        if root is None:
            return None
        return Node(root.val, self.invert_tree(root.right), self.invert_tree(root.left))