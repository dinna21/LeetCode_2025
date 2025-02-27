# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def height(root):
    if not root:
        return 0
    print(root.left)
    # left_height = height(root.left)
    # right_height = height(root.right)
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
    root = Node(12)
    root.left = Node(8)
    root.right = Node(18)
    root.left.left = Node(5)
    root.left.right = Node(11)

print(height(root))
# print(max(2,3))