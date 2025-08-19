# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.len_longest_seq = 1

    def dfs(self, node, pnode, longest_so_far):

        # if it is leaf node, it should be passed and not return as 
        #processing needs to continue
        if node.left is None and node.right is None:
            pass

        if node.val - pnode.val == 1:
            longest_so_far += 1
        else:
            longest_so_far = 1     

        if longest_so_far > self.len_longest_seq:
            self.len_longest_seq = longest_so_far

        if node.left is not None:
            self.dfs(node.left, node,longest_so_far)
        if node.right is not None:
            self.dfs(node.right, node, longest_so_far)    
        

    def longestConsecutive(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        self.dfs(root,root,0)
        return self.len_longest_seq

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
#root.left.left = BinaryTreeNode(3)
#root.left.right = BinaryTreeNode(4)
sol = Solution()
print(sol.longestConsecutive(root)) 