from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0  # base height for null nodes

            lheight = height(node.left)
            rheight = height(node.right)

            if lheight == -1 or rheight == -1 or abs(lheight - rheight) > 1:
                return -1  # signal unbalanced
            else:
                return 1 + max(lheight, rheight)  # height of this subtree

        return height(root) != -1  # if we get -1, tree is unbalanced
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

sol = Solution()
print(sol.isBalanced(root))
