class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
def invertTree(self, root):
    if root is None:
        return None
    left_inverted = invertTree(root.left)
    right_inverted = invertTree(root.right)
    root.left = right_inverted
    root.right = left_inverted
    return root
