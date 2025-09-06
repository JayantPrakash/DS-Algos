def topological_sort(n, edges):

    adj_list = [[] for _ in range(n)]

    for src,dist in edges:
        adj_list[src].append(dist)

    visited = [-1]*n
    linear_order = []

    def dfs(node):
        visited[node] = 1
        for neighbor in adj_list[node]:
            if visited[neighbor] == -1:
                dfs(neighbor)
        linear_order.append(node)            


    for i in range(n):
        if visited[i] == -1:
            dfs(i)
    linear_order.reverse()
    return linear_order


n = 5
edges = [[0, 1], [1, 2], [2,3],[3, 4]]

print(topological_sort(n,edges))

"""
We should add the elements in the list which is last visisted and finally reverse the list
to get topological sorting
T(n) = O(V+E)
S(n) = O(V + E) - E for adj list and V for stack and visited arrays
"""