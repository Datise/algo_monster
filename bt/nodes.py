class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class NonBNode():
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children