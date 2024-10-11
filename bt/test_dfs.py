import pdb
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