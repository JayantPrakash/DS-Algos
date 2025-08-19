class Solution(object):
    def dfs(self, node):
        self.visited[node] = 1
        if self.parent[node] == -1:
            self.color[node] = 0
        else:
            self.color[node] = 1 - self.color[self.parent[node]]
        for neigbor in self.graph[node]:
            if self.visited[neigbor] == -1:
                self.parent[neigbor] = node
                self.dfs(neigbor)
            else:
                if self.parent[node]!= neigbor:
                    if self.color[neigbor] == self.color[node]:
                        self.isBipartite = False
                        return False             
        return True


    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # Write your code here.
        self.visited = [-1]*len(graph)
        self.color = [-1]*len(graph)
        self.parent = [-1]*len(graph)
        self.isBipartite = True
        self.graph = graph
        for i in range(len(graph)):
            if self.visited[i] == -1:
                self.dfs(i)
        
        return self.isBipartite

sol = Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph = [[1,3],[0,2],[1,3],[0,2]]
print(sol.isBipartite(graph))

"""
Graph is bipartite if it has cycle and graph has odd length cycle.  
In dfs, if it is a cross edge and coloring of node and neigbor is same(odd length), 
it's not bipartite
In bfs, if it is a cross edge and distance(level) of node and neigbor is same(odd length), 
it's not bipartite

"""