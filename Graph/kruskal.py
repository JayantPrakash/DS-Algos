def kruskal(n,edges):
    parent = [i for i in range(n)]
    size = [1]*n
    mst_cost = 0
    mst = []
    edges = sorted(edges, key = lambda x : x[2])

    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x    
    
    for (u,v,cost) in edges:
        rootu = find(u)    
        rootv = find(v)

        if rootu != rootv:
            if size[rootu] >= size[rootv]:
                parent[rootv] = rootu
                size[rootu] += size[rootv]
            else:
                parent[rootu] = rootv
                size[rootv] += size[rootu]

            mst_cost += cost 
            mst.append([u,v])
    return mst_cost,mst

n = 4
edges = [(0, 1, 10), (1, 3, 15), (2, 3, 4), (2, 0, 6), (0, 3, 5)]
print(kruskal(n,edges))

"""
No of union operations = no of times it will merge that will be n-1
No of find operations = 2m, one find op cost logn as it will be balanced
sort - O(mlogm)
T(n) = n-1 * 1 + 2m*logn + O(mlogm)= O(nlogn)
S(n) = O(n)
"""