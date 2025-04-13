# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def print_Nodes(root):
    if root:
        print(root.val)
        print_Nodes(root.left)
        print_Nodes(root.right)
def diameterOfBinaryTree(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    left_diameter = diameterOfBinaryTree(root.left)
    right_diameter = diameterOfBinaryTree(root.right)
    return max(left_height + right_height + 1, max(left_diameter, right_diameter))

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(0)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    print(print_Nodes(root))