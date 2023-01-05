class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        mini=9999999
        vals=[[0 for j in range(n)] for i in range(m) ]
        vals[0][0]=grid[0][0]
        for i in range(1,m):
            vals[i][0]=vals[i-1][0]+grid[i][0]
        for i in range(1,n):
            vals[0][i]=vals[0][i-1]+grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                vals[i][j]=grid[i][j]+min(vals[i-1][j],vals[i][j-1])
        return vals[m-1][n-1]
            
        
        
                