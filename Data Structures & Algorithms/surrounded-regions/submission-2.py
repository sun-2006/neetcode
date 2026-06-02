class Solution:
    def solve(self, board: List[List[str]]) -> None:
        cols,rows=len(board[0]),len(board)
        visit=set()
        def dfs(r,c,visit):
            if ((r,c)in visit or r not in range(rows) or c not in range(cols) or 
                board[r][c]=="X"):
                return
            visit.add((r,c))
            board[r][c]="T"
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)
        for r in range(rows):
            dfs(r,0,visit)
            dfs(r,cols-1,visit)
        for c in range(cols):
            dfs(0,c,visit)
            dfs(rows-1,c,visit)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"
