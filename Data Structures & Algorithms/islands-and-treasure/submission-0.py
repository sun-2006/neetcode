class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q1=collections.deque()
        visit=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q1.append((r,c))
                    visit.add((r,c))
        while q1:
            ro,co=q1.popleft()
            d=1
            directions=[[0,1],[1,0],[-1,0],[0,-1]]
            for dr,dc in directions:
                ro1,co1=ro+dr,co+dc
                if (ro1 in range(rows) and
                    co1 in range(cols) and
                    (ro1,co1) not in visit and
                    grid[ro1][co1]!=-1):
                    grid[ro1][co1]=grid[ro][co]+1
                    q1.append((ro1,co1))
                    visit.add((ro1,co1))
            

