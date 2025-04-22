# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.left = None
#         self.right = None
# def areIdentical(root1,root2):
#     if root1 is None and root2 is None:
#         return True
#     if root1 is None or root2 is None:
#         return False
#     return (root1.data == root2.data) and areIdentical(root1.left,root2.left) and areIdentical(root1.right,root2.right)
# def isSubtree(root1,root2):
#     if root2 is None:
#         return True
#     if root1 is None:
#         return False
#     if areIdentical(root1,root2):
#         return True
#     return isSubtree(root1.left,root2) or isSubtree(root1.right,root2)


# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.areIdentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def areIdentical(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True 
        if root1 is None or root2 is None:
            return False 
        return (
            root1.val == root2.val and
            self.areIdentical(root1.left, root2.left) and
            self.areIdentical(root1.right, root2.right)
        )

# Example tree setup
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

subRoot = TreeNode(2)
subRoot.left = TreeNode(4)
subRoot.right = TreeNode(5)

sol = Solution()
print(sol.isSubtree(root, subRoot))

    