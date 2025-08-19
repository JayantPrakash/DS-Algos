from collections import deque

def number_of_connected_components(n, edges):

    # Write your code here.
    adj_list = [[] for _ in range(n)]

    for (src, dist) in adj_list:
        adj_list[src].append(dist)
        adj_list[dist].append(src)

    visited = [-1] * n
    def bfs(source):
        captured = [-1] * n
        
        q = deque()
        q.append(source)
        visited[source] = 1
        while(len(q)!=0):
            node = q.popleft()
            captured[node] = 1

            for neighbour in adj_list[node]:
                if visited[neighbour] == -1:
                    q.append(neighbour)
                    captured[neighbour] = 1

    num_components = 0

    for i in range(n):
        if visited[i] == -1:
            bfs(i)     
            num_components += 1
    return num_components                     

