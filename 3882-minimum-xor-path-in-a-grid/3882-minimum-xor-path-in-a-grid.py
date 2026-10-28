class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # m , n = len(grid),len(grid[0])
        # mini = float('inf')
        # def dfs(i,j,xor):

        #     nonlocal mini
        #     xor ^= grid[i][j]

        #     if i==m-1 and j==n-1:
        #         mini = min(mini,xor)
        #         return mini
        #     if i+1 < m:
        #         dfs(i+1,j,xor)
        #     if j+1 < n:
        #         dfs(i,j+1,xor)
            
        # dfs(0,0,0)
        # return mini

        m, n = len(grid), len(grid[0])

        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(set())
            dp.append(row)

        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if i > 0:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ grid[i][j])

                if j > 0:
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ grid[i][j])

        return min(dp[m - 1][n - 1])
            
        