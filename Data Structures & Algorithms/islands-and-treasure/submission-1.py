import collections
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        q1 = collections.deque()
        INF = 2147483647
        
        # Step 1: Find all multi-source starting points (treasure chests)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q1.append((r, c))
                    # No visit set needed!
        
        # Define directions ONCE outside the loop
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # Step 2: Multi-source BFS
        while q1:
            ro, co = q1.popleft()
            
            for dr, dc in directions:
                ro1, co1 = ro + dr, co + dc
                
                # Chained boundary check + check if it's an unvisited land cell (INF)
                if (0 <= ro1 < rows and 
                    0 <= co1 < cols and 
                    grid[ro1][co1] == INF): 
                    
                    # Update distance in-place based on the parent cell
                    grid[ro1][co1] = grid[ro][co] + 1
                    q1.append((ro1, co1))