#Definition for a binary tree node.
from typing import Optional
from typing import List
from collections import deque
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None : return []
        queue = deque()
        queue.append(root)
        result = []
        while len(queue)!=0 : 
            result.append([elem.val for elem in queue])
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.popleft()
                if node.children is not None:
                    for child in node.children:
                            queue.append(child)  
        return result

root = Node(10)
root.children = [Node(11),Node(9),Node(5)]
sol = Solution()
print(sol.levelOrder(root))

# time complexity - O(n)
# space complexity - O(n)
     