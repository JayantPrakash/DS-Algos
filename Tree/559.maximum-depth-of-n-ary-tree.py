
# Definition for a Node.
class TreeNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):

    def dfs(self,node, depth):
        # node.children == None will not work, so check with size of children
        if len(node.children) == 0:
            if self.max_depth < depth:
                self.max_depth = depth
        for child in node.children:
            self.dfs(child, depth + 1)     

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.max_depth = 1
        if root is None:
            return 0
        self.dfs(root,self.max_depth)
        return self.max_depth
    
root = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root.children = [node2,node3, node4]
node2.children = [node5,node6]
#root.left.left = BinaryTreeNode(3)
#root.left.right = BinaryTreeNode(4)
sol = Solution()
print(sol.maxDepth(root))     

#T(n) = O(n)
#S(n) = O(n)