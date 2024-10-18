# global var for educational purposes to show
# different return strategies
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
        def max_depth(node):
            if node is root:
                return 0

            return max(max_depth(root.left), max_depth(root.right)) + 1

        return max_depth(root) - 1 if root else 0

    def visible_tree_nodes(self, node, prev_vals=None):

        if node is None:
            return 0

        biggest = 0
        if prev_vals is None:
            prev_vals = []
            biggest = 1

        for val in prev_vals:
            if node.val > val:
                biggest = 1

        prev_vals.append(node.val)

        left = self.visible_tree_nodes(node.left, prev_vals)
        right = self.visible_tree_nodes(node.right, prev_vals)

        return max(left, right) + biggest