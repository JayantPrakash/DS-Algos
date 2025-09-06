# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):      
    
    def dfs(self, node):
        if node.left is None and node.right is None:
            return 0
        
        my_dia = left_dia = right_dia = 0

        if node.left is not None:
            left_dia = self.dfs(node.left) + 1

        if node.right is not None:
            right_dia = self.dfs(node.right) + 1
        
        my_dia = left_dia + right_dia
        if my_dia > self.max_len:
            self.max_len = my_dia    
        return max(left_dia,right_dia)   


    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        self.max_len = 0
        self.dfs(root)
        return self.max_len

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
#root.left.left = BinaryTreeNode(3)
#root.left.right = BinaryTreeNode(4)
sol = Solution()
print(sol.diameterOfBinaryTree(root))      