# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def dfs(self, node):
        
        if node.left is None and node.right is None:
            self.unival_count += 1
            return True
        is_node_unival = True
        if node.left is not None:
            is_left_unival = self.dfs(node.left)
            if is_left_unival and node.val == node.left.val:
                is_node_unival = True
            else:
                is_node_unival = False   
        if node.right is not None:
            is_right_unival = self.dfs(node.right)
            if is_right_unival and node.val == node.right.val:
                is_node_unival = True
            else:
                is_node_unival = False    
        
        if node.left is not None and node.right is not None:
            if is_left_unival and is_right_unival and (node.val == node.left.val == node.right.val):
                is_node_unival = True
            else:
                is_node_unival = False   
        
        if is_node_unival:
            self.unival_count += 1

        return is_node_unival

    def countUnivalSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.unival_count = 0
        self.dfs(root)
        return self.unival_count      

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