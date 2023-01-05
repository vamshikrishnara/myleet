class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        val= [ [ 0 for i in range(n) ] for j in range(m) ]
        for i in range(n):
            val[0][i]=1
        for j in range(m):
            val[j][0]=1
        for i in range(1,m):
            for j in range(1,n):
                val[i][j]=val[i-1][j]+val[i][j-1]
        return val[m-1][n-1]
        
                    