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


# /////////////////////////////////////Explanation /////////////////////////////
# 🔍 What They Mean:
# if subRoot is None: return True

# An empty tree (None) is considered a subtree of any tree.

# ✅ This returns True.

# if root is None: return False

# A non-empty subRoot cannot be a subtree of an empty root.

# ❌ This returns False.

# root
      1
     / \
    2   3
   / \
  4   5
# subRoot
    2
   / \
  4   5

# ✅ Step-by-Step Execution
# Call: isSubtree(root=1, subRoot=2)
# subRoot is not None → ✅

# root is not None → ✅

# Call: areIdentical(root1=1, root2=2)

# areIdentical(1, 2)
# 1 != 2 → ❌ return False

# So now we check:

# python
# Copy code
# return isSubtree(root.left=2, subRoot=2) or isSubtree(root.right=3, subRoot=2)
# Call: isSubtree(root=2, subRoot=2)
# subRoot is not None → ✅

# root is not None → ✅

# Call: areIdentical(2, 2)

# areIdentical(2, 2)
# 2 == 2 → ✅

# Recursively check:

# areIdentical(4, 4) → ✅

# 4 == 4, children are both None → ✅

# areIdentical(5, 5) → ✅

# 5 == 5, children are both None → ✅

# So whole tree matches → ✅ return True

# ✅ Therefore, isSubtree(root=2, subRoot=2) returns True

# So final result of the original call:

# python
# Copy code
# isSubtree(root=1, subRoot=2) => True
# 🔁 Recap of the Logic
# Here’s how it works at each node in root:

# It compares the subtree rooted at the current node (root) with subRoot using areIdentical().

# If they match, return True.

# If not, it moves left and right in root recursively to see if subRoot matches any subtree.

# 🧠 Visualization of Recursive Calls:
# text
# Copy code
# isSubtree(1, 2)
# ├── areIdentical(1, 2) → False
# ├── isSubtree(2, 2)
# │   └── areIdentical(2, 2) → True ✅
# └── [no need to check right side since match is found]