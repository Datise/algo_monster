import unittest
from bt import build_tree, print_tree
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
        self.assertEqual(4, num_visible)

    def test_is_balanced(self):
        test_tree = iter("3 4 5 x x 7 x x 8 x x".split())
        root = build_tree(test_tree, int)
        balanced = DFS().is_balanced(root)
        self.assertEqual(True, balanced)

    def test_is_balanced(self):
        test_tree = iter("3 4 5 x x 7 x x 8 x x".split())
        root = build_tree(test_tree, int)
        balanced = DFS().is_balanced(root)
        self.assertEqual(True, balanced)

    def test_is_not_balanced(self):
        test_tree = iter("3 4 5 x x 7 10 14 22 x x x x x 8 x x".split())
        root = build_tree(test_tree, int)
        balanced = DFS().is_balanced(root)
        self.assertEqual(False, balanced)

    def test_is_balanced_only_root(self):
        test_tree = iter("3".split())
        root = build_tree(test_tree, int)
        balanced = DFS().is_balanced(root)
        self.assertEqual(True, balanced)

    def test_is_balanced_root_plus_1(self):
        test_tree = iter("3 4 x".split())
        root = build_tree(test_tree, int)
        balanced = DFS().is_balanced(root)
        self.assertEqual(True, balanced)

    def test_is_unbalanced_one_sided(self):
        test_tree = iter("3 4 5 6 7 x x x x x x".split())
        root = build_tree(test_tree, int)
        balanced = DFS().is_balanced(root)
        self.assertEqual(False, balanced)

    def test_is_sub_tree(self):
        root = build_tree(iter("3 4 5 6 x x 7".split()), int)
        sub_root = build_tree(iter("5 6 x x 7".split()), int)
        same = DFS().subtree_of_another_tree(root, sub_root)
        self.assertEqual(True, same)

    def test_is_sub_tree_btm(self):
        root = build_tree(iter("3 4 5 6 x x 7 8 9 x x".split()), int)
        sub_root = build_tree(iter("7 8 9 x x".split()), int)
        same = DFS().subtree_of_another_tree(root, sub_root)
        self.assertEqual(True, same)

    def test_is_not_sub_tree(self):
        root = build_tree(iter("3 4 5 6 x x 7".split()), int)
        sub_root = build_tree(iter("5 4 x x 7".split()), int)
        same = DFS().subtree_of_another_tree(root, sub_root)
        self.assertEqual(False, same)