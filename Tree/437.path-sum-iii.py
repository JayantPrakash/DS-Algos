# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def dfs(self, node, targetSum, slate):
        if node.left is None and node.right is None:
            pass
        slate.append(node.val)
        # Every time dfs calls, it checks from the last element 
        # to the top if it is summing to target sum
        suffix_sum = 0
        for i in range(len(slate)-1,-1,-1):
            suffix_sum += slate[i]
            if suffix_sum == targetSum:
                self.count_path += 1
        if node.left is not None:
            self.dfs(node.left,targetSum, slate)
        if node.right is not None:
            self.dfs(node.right,targetSum, slate)
        
        slate.pop()

    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.global_box = []
        if root is None:
            return 0
        self.count_path = 0

        self.dfs(root,targetSum,[])

        return self.count_path,self.global_box
    

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
#root.left.left = BinaryTreeNode(3)
#root.left.right = BinaryTreeNode(4)
sol = Solution()
print(sol.pathSum(root,5))     

# Every time dfs calls, it checks from the last element 
# to the top if it is summing to target sum
#T(n) = O(n^2)
#S(n) = O(n)