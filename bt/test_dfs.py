import unittest
from bt import build_tree
from dfs import DFS

class TestDFS(unittest.TestCase):
    def test_dfs(self):
        test_tree = iter("3 4 5 x x 7 x x 8 x x".split())
        root = build_tree(test_tree, int)
        found = DFS().search(root, 7)
        self.assertEqual(found.val, 7)
        found4 = DFS().search(root, 4)
        self.assertEqual(4, found4.val)

    def test_dfs_single_tree(self):
        test_tree = iter("3".split())
        root = build_tree(test_tree, int)
        found3 = DFS().search(root, 3)
        self.assertEqual(3, found3.val)

    def test_dfs_global_search(self):
        test_tree = iter("3 4 5 x x 7 x x 8 x x".split())
        root = build_tree(test_tree, int)
        found = DFS().search_global(root, 5)
        self.assertEqual(5, found.val)

    def test_dfs_find_highest(self):
        test_tree = iter("3 4 5 x x 7 x x 8 x x".split())
        root = build_tree(test_tree, int)
        highest = DFS().find_highest_val(root)
        self.assertEqual(8, highest)

    def test_dfs_find_max_depth(self):
        test_tree = iter("3 4 5 x x 7 x x 8 x x".split())
        root = build_tree(test_tree, int)
        depth = DFS().find_max_depth(root)
        self.assertEqual(2, depth)

    def test_visible_tree_nodes(self):
        test_tree = iter("3 4 5 x x 7 x x 8 x x".split())
        root = build_tree(test_tree, int)
        num_visible = DFS().visible_tree_nodes(root)
        self.assertEqual(5, num_visible)

    def test_vis_tree_nodes_rev(self):
        test_tree = iter("5 4 3 x x 8 x x 6 x x".split())
        root = build_tree(test_tree, int)
        num_visible = DFS().visible_tree_nodes(root)
        self.assertEqual(3, num_visible)

    def test_vis_tree_nodes_interior(self):
        test_tree = iter("5 4 3 x 9 8 10 12 6 7 x x 9 x x".split())
        root = build_tree(test_tree, int)
        num_visible = DFS().visible_tree_nodes(root)
        self.assertEqual(8, num_visible)