import collections
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Convert deadends to a set for O(1) lookups (Crucial to avoid TLE)
        deadset = set(deadends)
        if "0000" in deadset:
            return -1
            
        visit = set()
        initial = "0000"
        q = collections.deque()
        
        # Keep your exact structure: queue stores (combination_string, depth)
        q.append((initial, 0))
        visit.add(initial) # Mark initial as visited
        
        while q:
            value, d = q.popleft()
            
            if value == target:
                return d
                
            # Generate all 8 possible children from the current state
            for i in range(4):
                digit = int(value[i])
                
                # Turn wheel up (+1) and turn wheel down (-1) with wrap-around
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    # Reconstruct the string using slices
                    child = value[:i] + str(new_digit) + value[i+1:]
                    
                    if child not in visit and child not in deadset:
                        visit.add(child)
                        q.append((child, d + 1))
                        
        return -1