class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        mat=[[float('inf')]*26 for i in range(26)]
        for i in range(26):
            mat[i][i]=0
        for k in range(len(cost)):
            i=ord(original[k])-ord('a')
            j=ord(changed[k])-ord('a')
            mat[i][j]=min(mat[i][j],cost[k])
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    mat[i][j]=min(mat[i][j],mat[i][k]+mat[k][j])
        res=0
        for k in range(len(source)):
            i=ord(source[k])-ord('a')
            j=ord(target[k])-ord('a')
            if mat[i][j]==float('inf'):
                return -1
            res+=mat[i][j]
        return res