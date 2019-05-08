import numpy as np
class Solution(object):
    def __init__(self):
        self.d = [[-1,0], [0,1], [1,0], [0,-1]]
        self.m = 0
        self.n = 0
        self.visited = list()
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.m = len(grid)
        if self.m == 0:
            return 0
        self.n = len(grid[0])
        self.visited = np.zeros((self.m, self.n))
        res = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1' and self.visited[i][j] != 1:
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def dfs(self, grid, x, y):
        self.visited[x][y] = 1
        for i in range(4):
            newx = x + self.d[i][0]
            newy = y + self.d[i][1]
            if self.inArea(newx,newy) and self.visited[newx][newy] != 1 and grid[newx][newy] == '1':
                self.dfs(grid, newx, newy)
        return
