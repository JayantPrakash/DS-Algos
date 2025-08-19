from collections import deque

class Graph:
    def __init__(self,n):
        self.visited = [-1] * n    
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
                self.dfs(neighbor,adjList)
        print(source)
n = 5
edges = [[0, 1], [1, 2], [0, 2], [2,3],[3, 4]]
#edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
source = 0
g = Graph(n)
adjList = g.createAdjacencyList(n, edges)
#print(adjList)
g.dfs(source, adjList)
