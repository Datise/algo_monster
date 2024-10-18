# global var for educational purposes to show
# different return strategies
import pdb

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
        def visible(node, prev_vals):
            if node is None:
                return 0

            biggest = 0
            if len(prev_vals) is 0:
                biggest = 1

            for val in prev_vals:
                if node.val > val:
                    biggest = 1

            prev_vals.append(node.val)

            left = visible(node.left, prev_vals)
            right = visible(node.right, prev_vals)

            prev_vals.pop()
            return left + right + biggest

        return visible(root, [])