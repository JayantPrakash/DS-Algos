import heapq
def dijkstra(n,edges,src):
    adj_list = [[] for _ in range(n)]
    for u,v,cost in edges:
        adj_list[u].append((v,cost))
        adj_list[v].append((u,cost))

    pq = []
    dist = [float('inf')]*n 
    captured = [-1]*n
    dist[0] = 0

    heapq.heappush(pq,[0,src])

    while pq:
        cost, node = heapq.heappop(pq)
        captured[node] = 1

        for neighbor, cost in adj_list[node]:
            if captured[neighbor] == -1:
                if  dist[neighbor] > cost + dist[node]:
                    dist[neighbor] = cost + dist[node]
                    heapq.heappush(pq,[dist[neighbor], neighbor])    
    return dist


n = 4
edges = [(0, 1, 10), (1, 3, 15), (2, 3, 4), (2, 0, 6), (0, 3, 5)]
print(dijkstra(n,edges,0))

"""
Time Complexity: O(E*logV), Where E is the number of edges and V is the number of vertices.
Auxiliary Space: O(V)
"""