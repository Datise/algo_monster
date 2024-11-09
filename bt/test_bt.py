import unittest

from bt import *

class TestBT(unittest.TestCase):
    def test_build_tree(self):
        test_tree = iter("3 4 5 x x 7 x 8 9".split())
        root = build_tree(test_tree, int)
        self.assertEqual(root.val, 3)

    def test_search(self):
        root = build_tree(iter("6 4 3 x x 5 x x 8 x 9".split()), int)
        self.assertEqual(8, search_bts(root, 8))

    def test_validate_bts(self):
        root = build_tree(iter("6 4 3 x x 5 x x 8 x 9".split()), int)
        self.assertEqual(True, validate_bts(root))

    def test_validate_bts_bad_root(self):
        root = build_tree(iter("2 4 3 x x 5 x x 8 x 9".split()), int)
        self.assertEqual(False, validate_bts(root))
    
    def test_validate_bts_wrong_side(self):
        root = build_tree(iter("2 4 3 x x 5 x x 8 9".split()), int)
        self.assertEqual(False, validate_bts(root))
    
    def test_ternary_paths(self):
        root = build_mc_tree(iter("1 3 2 0 3 0 4 3 5 0 6 0 7 0".split()), int)
        #print_mc_tree(root, 0)
        res = ternary_tree_paths(root)
        self.assertEqual(['1->2', '1->3', '1->4->5', '1->4->6', '1->4->7'], res)