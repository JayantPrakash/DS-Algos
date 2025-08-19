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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = deque()
        queue.append(root)
        do_reverse = False
        result = []
        temp_list = []
        while(len(queue) != 0):
            temp_list = [elem.val for elem in queue]
            if do_reverse:
                temp_list.reverse()
                do_reverse = False
            else:
                do_reverse = True
            
            result.append(temp_list)
            len_queue = len(queue)
            for _ in range(len_queue):
                node = queue.popleft()

                if node.left is not None:
                    queue.append(node.left)   

                if node.right is not None:
                    queue.append(node.right)      
     
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

sol = Solution()
print(sol.zigzagLevelOrder(root))

#T(n) = O(n)
#S(n) = O(n)        