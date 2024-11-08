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