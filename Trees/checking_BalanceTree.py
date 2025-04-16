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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and self.isSameTree(p.left,q.left)
                and self.isSameTree(p.right,q.right))
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
tree1 = TreeNode(4)
tree1.right = TreeNode(5)
tree1.left = TreeNode(3)
tree2 = TreeNode(4)
tree2.right = TreeNode(5)
tree2.left = TreeNode(3)
sol = Solution()
print(sol.isBalanced(root))
print(sol.isSameTree(tree1,tree2))
