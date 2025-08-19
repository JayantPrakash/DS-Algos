# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.len_longest_seq = 1
    def dfs(self, node, slate):

        if node.left is None and node.right is None:
            slate.append(node)

            temp_li = [node.val]
            #temp_li.append(node.val)

            for i in range(len(slate)-1):
                if slate[i+1].val - slate[i].val == 1:
                    temp_li.append(slate[i+1].val)
                    if i == len(slate)-2:
                        if self.len_longest_seq < len(temp_li):
                            self.len_longest_seq = len(temp_li)

                else:
                    if self.len_longest_seq < len(temp_li):
                        self.len_longest_seq = len(temp_li)
                    temp_li = [slate[i+1].val]
            slate.pop()

        slate.append(node)

        if node.left is not None:
            self.dfs(node.left, slate)
        if node.right is not None:
            self.dfs(node.right, slate)    
        
        slate.pop()

    def longestConsecutive(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        self.dfs(root,[])
        return self.len_longest_seq

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
#root.left.left = BinaryTreeNode(3)
#root.left.right = BinaryTreeNode(4)
sol = Solution()
print(sol.longestConsecutive(root)) 