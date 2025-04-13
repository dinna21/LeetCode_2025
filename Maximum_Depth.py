# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    print(root.right)
    # print(max(left_height, right_height))
    # return 1 + max(left_height, right_height)
# Example usage:
    # Representation of the input tree:
    #     12
    #    /  \
    #   8   18
    #  / \
    # 5   11
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(0)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)

print(height(root))
# print(max(2,3))