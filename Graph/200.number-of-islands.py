class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def find_neighbors(x,y):
            results = []
            if x + 1  < len(grid):
                results.append((x+1,y))
            if x - 1 >= 0:
                results.append((x-1,y))
            if y + 1 < len(grid[0]):
                results.append((x,y+1))
            if y - 1 >= 0:
                results.append((x,y-1))
            return results
        
        def dfs(i,j):
            grid[i][j] = '0'
            neigbors = find_neighbors(i,j)

            for (nr,nc) in neigbors:
                if grid[nr][nc]!= '0':
                    dfs(nr,nc)

        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != '0':
                    dfs(x,y)
                    islands += 1
        return islands

sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sol.numIslands(grid)) 

"""
find the neigbors of the node
if visited, make the node as '0'. If it encounters '0', it can't traverse
Count no of connected components
if grid[x][y] != '0':
    dfs(x,y)
"""