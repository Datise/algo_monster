import unittest

from bt import build_tree


class TestBT(unittest.TestCase):
    def test_build_tree(self):
        test_tree = iter("3 4 5 x x 7 x 8 9".split())
        root = build_tree(test_tree, int)
        self.assertEqual(root.val, 3)

