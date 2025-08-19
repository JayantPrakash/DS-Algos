from collections import deque

#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    if root.left is not None:
        dfs(root.left)
    
    if root.right is not None:
        dfs(root.right)
    print(root.value)

root = BinaryTreeNode(10)
root.left = BinaryTreeNode(11)
root.right = BinaryTreeNode(9)
dfs(root)

#preorder dfs
#T(n) = O(n)
#S(n) = O(n)