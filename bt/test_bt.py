import unittest

from bt import build_tree


class TestBT(unittest.TestCase):
    def test_build_tree(self):
        testTree = iter("3 4 5 x x 7 x 8 9".split())
        result = build_tree(testTree, int)
        print(result)

