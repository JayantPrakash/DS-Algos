from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def dfs(self,node,sum,slate):
        if node.left is None and node.right is None:
            if sum - node.val == 0:
                slate.append(node.val)
                self.global_box.append(slate[:])
                slate.pop()
            return

        slate.append(node.val)
        if node.left is not None:
            self.dfs(node.left, sum - node.val,slate)
        
        if node.right is not None:
            self.dfs(node.right, sum - node.val,slate)
        
        slate.pop()


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.global_box = []  
        self.dfs(root, targetSum, [])
        return self.global_box
        
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
#root.left.left = BinaryTreeNode(3)
#root.left.right = BinaryTreeNode(4)
sol = Solution()
print(sol.pathSum(root,4))     