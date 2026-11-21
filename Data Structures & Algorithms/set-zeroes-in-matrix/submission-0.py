class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        c=len(matrix[0])
        markr,markc=[False]*r,[False]*c
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    markr[i]=True
                    markc[j]=True
        for i in range(r):
            for j in range(c):
                if markr[i] or markc[j]:
                    matrix[i][j]=0
                    
        