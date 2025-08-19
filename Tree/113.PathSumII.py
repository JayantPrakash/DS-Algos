class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
          
    def dfs(self,node,sum,slate):
        if node.left is None and node.right is None:
            slate.append(node.val)
            if sum - node.val == 0:
                self.global_box.append[slate[:]]
                slate.pop()
                return

        slate.append(node.val)
        if node.left is not None:
            return self.dfs(node.left, sum - node.left.val,slate)
        
        if node.right is not None:
            return self.dfs(node.right, sum - node.right.val,slate)
        
        slate.pop()


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if root is None:
            return []
        self.global_box = []  
        self.dfs(root, targetSum, [])
        return self.global_box
        
        