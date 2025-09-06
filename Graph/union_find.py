def union_find(n,edges):
    parent = [i for i in range(n)]
    size = [1]*n
    components = n

    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x    
    
    for u,v in edges:
        rootu = find(u)    
        rootv = find(v)

        if rootu != rootv:
            if size[rootu] >= size[rootv]:
                parent[rootv] = rootu
                size[rootu] += size[rootv]
            else:
                parent[rootu] = rootv
                size[rootv] += size[rootu]

            components -= 1        
    return components

n = 5
edges = [[0, 1], [1, 2],[0, 2], [2,3],[3, 4]]
edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
print(union_find(n,edges))

"""
No of union operations = no of times it will merge that will be n-1
No of find operations = 2m, one find op cost logn as it will be balanced

T(n) = n-1 * 1 + 2m*logn = O(mlogn)
S(n) = O(n)
"""