from collections import deque

def number_of_connected_components(n, edges):

    # Write your code here.
    adj_list = [[] for _ in range(n)]

    for (src, dist) in edges:
        adj_list[src].append(dist)
        adj_list[dist].append(src)

    visited = [-1] * n

    def bfs(source):      
        q = deque()
        q.append(source)
        visited[source] = 1
        while(len(q)!=0):
            node = q.popleft()
            for neighbour in adj_list[node]:
                if visited[neighbour] == -1:
                    q.append(neighbour)
                    visited[neighbour] = 1

    num_components = 0

    for i in range(n):
        if visited[i] == -1:
            bfs(i)     
            num_components += 1
    return num_components                     

n = 7
edges = [[0, 1], [1, 2], [0, 2], [2,3],[3, 4],[5,6]]
print(number_of_connected_components(n, edges))