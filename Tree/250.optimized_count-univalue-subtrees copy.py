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
            if not is_left_unival or node.val != node.left.val:
                is_node_unival = False   
        if node.right is not None:
            is_right_unival = self.dfs(node.right)
            if not is_right_unival or node.val != node.right.val:
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
root.right = TreeNode(3)
#root.left.left = BinaryTreeNode(3)
#root.left.right = BinaryTreeNode(4)
sol = Solution()
print(sol.countUnivalSubtrees(root))     

# both left and right subtree should be true and
# node value should be equal to left and right child value
#T(n) = O(n)
#S(n) = O(n)