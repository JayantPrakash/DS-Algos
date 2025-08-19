class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def dfs(self,node,sum):
        if node.left is None and node.right is None:
            if sum - node.val == 0:
                self.global_box = True
            return

        if node.left is not None:
            self.dfs(node.left, sum - node.val)
        
        if node.right is not None:
            self.dfs(node.right, sum - node.val)
        
        
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        self.global_box = False  
        self.dfs(root, targetSum)
        return self.global_box