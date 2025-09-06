from collections import deque

class Solution(object):
    def createAdjacencyList(self, n, edges):
        adj_list = [[] for _ in range(n)]

        for (src,dist) in edges:
            adj_list[src].append(dist)
            adj_list[dist].append(src)
        
        return adj_list
 
    def dfs(self, source, adjList):
        self.visited[source] = 1

        for neighbor in adjList[source]:
            if self.visited[neighbor] == -1:
                self.parent[neighbor] = source
                if not self.dfs(neighbor,adjList):
                    return False
            else:
                if self.parent[source] != neighbor:
                    return False
        return True        

    def validTree(self, n, edges):
        self.visited = [-1] * n    
        self.parent = [-1] * n
        adj_list = self.createAdjacencyList(n,edges)
        num_components = 0
        for v in range(n):
            if self.visited[v] == -1:
                is_valid_tree = self.dfs(v, adj_list)
                if is_valid_tree == False:
                    return False
                num_components += 1
        if num_components > 1:
            return False
        return is_valid_tree
        


n = 5
edges = [[0, 1], [1, 2],[0, 2], [2,3],[3, 4]]
#edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
edges = [[0,1],[2,3]]
source = 0
g = Solution()
#adjList = g.createAdjacencyList(n, edges)
#print(adjList)
print(g.validTree(n,edges))

"""
graph will not be tree if it has cycle and has more than 1 connected components.
self.parent[source] != neighbor: return False

T(n) = O(n)
S(n) = O(n)
"""

