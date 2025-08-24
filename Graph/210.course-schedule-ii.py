class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = [[] for _ in range(numCourses)]

        for dist,src in prerequisites:
            adj_list[src].append(dist)
        print(adj_list)
        visited = [-1]*numCourses
        arr = [-1]*numCourses
        dep = [-1]*numCourses
        timestamp = [0]
        order_course = []
        def dfs(node):
            visited[node] = 1
            arr[node] = timestamp[0]
            timestamp[0] += 1
            for neighbor in adj_list[node]:
                if visited[neighbor] == -1:
                    if dfs(neighbor) is False:
                        return False                        
                else:
                    if dep[neighbor] == -1:
                        return False
            dep[node] = timestamp[0]
            timestamp[0] += 1
            order_course.append(node)
            return True
        for i in range(numCourses):
            if visited[i] == -1:
                if dfs(i) == False:
                    return []
        order_course.reverse()
        return order_course

numCourses = 2
prerequisites = [[1,0],[0,1]]
prerequisites = [[1,0]]
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
sol = Solution()
print(sol.findOrder(numCourses,prerequisites))

"""
If there is back edge, then its having cycle, depature of destination is not set, 
then its back edge if destination is visited previously, return []
otherwise append in the list in the order of decreasing dep. Finally reverse the order,
its called topological sorting

T(n) = O(V+E)
S(n) = O(V+E)

"""