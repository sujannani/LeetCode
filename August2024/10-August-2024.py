class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(i,j):
            if i<0 or i>=n*3 or j<0 or j>=n*3 or mat[i][j]==1:
                return
            mat[i][j]=1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        n=len(grid)
        mat=[[0]*n*3 for i in range(n*3)]
        for i in range(n):
            k,j=0,0
            while k<len(grid[i]):
                if grid[i][k]=='/':
                    mat[i*3][j*3+2]=1
                    mat[i*3+1][j*3+1]=1
                    mat[i*3+2][j*3]=1
                    k+=1
                elif grid[i][k]==' ':
                    k+=1
                else:
                    mat[i*3+1][j*3+1]=1
                    mat[i*3][j*3]=1
                    mat[i*3+2][j*3+2]=1
                    k+=1
                j+=1
        count=0
        for i in range(n*3):
            for j in range(n*3):
                if mat[i][j]==0:
                    count+=1
                    dfs(i,j)
        return count