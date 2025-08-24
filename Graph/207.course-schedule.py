class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = [[] for _ in range(numCourses)]

        for dist,src in prerequisites:
            adj_list[src].append(dist)
        visited = [-1]*numCourses
        arr = [-1]*numCourses
        dep = [-1]*numCourses
        timestamp = [0]
        def dfs(node):
            visited[node] = 1
            arr[node] = timestamp[0]
            timestamp[0] = timestamp[0] + 1 
            for neighbor in adj_list[node]:
                if visited[neighbor] == -1:
                    if dfs(neighbor) is False:
                        return False                        
                else:
                    if dep[neighbor] == -1:
                        return False
            dep[node] = timestamp[0]
            timestamp[0] = timestamp[0] + 1 
            return  True
        
        for i in range(numCourses):
            if visited[i] == -1:
                if dfs(i) == False:
                    return False
        return True

numCourses = 2
prerequisites = [[1,0],[0,1]]
#prerequisites = [[1,0]]

sol = Solution()
print(sol.canFinish(numCourses,prerequisites))

"""
If there is back edge, then its having cycle, depature of destination is not set, 
then its back edge if destination is visited previously

T(n) = O(V+E)
S(n) = O(V+E)
"""