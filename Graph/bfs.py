from collections import deque

class Graph:

    def createAdjacencyList(self, n, edges):
        adj_list = [[] for _ in range(n)]

        for (src,dist) in edges:
            adj_list[src].append(dist)
            adj_list[dist].append(src)
        
        return adj_list
 
    def bfs(self, source, adjList):
        visited = [-1] * n
        visited[source] = 1
        q = deque()
        q.append(source)

        while len(q)!=0:
            node = q.popleft()
            print(node)
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:
                    q.append(neighbor)
                    visited[neighbor] = 1    


n = 5
edges = [[0, 1], [1, 2], [0, 2], [2,3],[3, 4]]
#edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
source = 0
g = Graph()
adjList = g.createAdjacencyList(n, edges)
print(adjList)
g.bfs(source, adjList)
