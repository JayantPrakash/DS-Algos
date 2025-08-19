
"""
For your reference:
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    from collections import deque
    if root is None:
        return []
    Q = deque()
    Q.append(root)
    result = []
    while len(Q) != 0:
        len_Q = len(Q)
        result.append([e.value for e in Q])
        for i in range(len_Q):
            node = Q.popleft()
            if node.left is not None:
                Q.append(node.left)
            if node.right is not None:
                Q.append(node.right)
    return result

root = BinaryTreeNode(10)
root.left = BinaryTreeNode(11)
root.right = BinaryTreeNode(9)
print(level_order_traversal(root))

# time complexity - O(n)
# space complexity - O(n)
