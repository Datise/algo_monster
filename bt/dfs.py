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