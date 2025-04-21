class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
def areIdentical(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.data == root2.data) and areIdentical(root1.left,root2.left) and areIdentical(root1.right,root2.right)
def isSubtree(root1,root2):
    if root2 is None:
        return True
    if root1 is None:
        return False
    if areIdentical(root1,root2):
        return True
    