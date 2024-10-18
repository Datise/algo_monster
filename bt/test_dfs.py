import unittest
from bt import build_tree
from dfs import DFS

class TestDFS(unittest.TestCase):
    def test_dfs(self):
        test_tree = iter("3 4 5 x x 7 8".split())
        root = build_tree(test_tree, int)
        found = DFS().search(root, 7)
        self.assertEqual(found.val, 7)
        found4 = DFS().search(root, 4)
        self.assertEqual(found4.val, 4)

    def test_dfs_single_tree(self):
        test_tree = iter("3".split())
        root = build_tree(test_tree, int)
        found3 = DFS().search(root, 3)
        self.assertEqual(found3.val, 3)

    def test_dfs_global_search(self):
        test_tree = iter("3 4 5 x x 7 8".split())
        root = build_tree(test_tree, int)
        found = DFS().search_global(root, 5)
        self.assertEqual(found.val, 5)

    def test_dfs_find_highest(self):
        test_tree = iter("3 4 5 x x 7 8".split())
        root = build_tree(test_tree, int)
        highest = DFS().find_highest_val(root)
        self.assertEqual(highest, 8)

    def test_dfs_find_max_depth(self):
        test_tree = iter("3 4 5 x x 7 8".split())
        root = build_tree(test_tree, int)
        depth = DFS().find_max_depth(root)
        self.assertEqual(depth, 2)

    def test_visible_tree_nodes(self):
        test_tree = iter("3 4 5 x x 7 8".split())
        root = build_tree(test_tree, int)
        num_visible = DFS().visible_tree_nodes(root)
        self.assertEqual(num_visible, 4)

    # def test_visible_tree_nodes_rev(self):
    #     test_tree = iter("5 4 3 x x 8 x x 6".split())
    #     root = build_tree(test_tree, int)
    #     num_visible = DFS().visible_tree_nodes(root)
    #     self.assertEqual(num_visible, 3)