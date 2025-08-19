#Definition for a binary tree node.
from typing import Optional
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bfs(self, root: Optional[TreeNode]):
        queue = deque()
        queue.append(root)
        
        while len(queue)!=0 :
            node = queue.popleft()
            print(node.val)  

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)    


root = TreeNode(10)
root.left = TreeNode(11)
root.right = TreeNode(9)
sol = Solution()
sol.bfs(root)

#T(n) = O(n)
#S(n) = O(n)        