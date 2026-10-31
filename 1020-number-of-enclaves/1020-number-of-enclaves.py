class Solution:
    def dfs(self,grid,ones,r,c):
        m =len(grid)
        n =len(grid[0])
        if r > m-1 or r<0 or c>n-1 or c<0:
            return ones 
        
        if grid[r][c]==0:
            return ones
        
        
        
        ones-=1
        grid[r][c]=0
        
        ones=self.dfs(grid,ones,r-1,c)
        ones=self.dfs(grid,ones,r+1,c)
        ones=self.dfs(grid,ones,r,c-1)
        ones=self.dfs(grid,ones,r,c+1)

        return ones

        
    def numEnclaves(self, grid: list[list[int]]) -> int:
        ones = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ones+=1

        for i in range(m):
            ones=self.dfs(grid,ones,i,0)
            ones=self.dfs(grid,ones,i,n-1)
            
        for j in range(n):
            ones=self.dfs(grid,ones,0,j)
            ones=self.dfs(grid,ones,m-1,j)
        

        
        return ones

        