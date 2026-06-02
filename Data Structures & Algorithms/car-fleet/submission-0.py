class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l=[(p,s) for p,s in zip(position,speed)]
        l.sort(reverse=True)
        s=[]
        for p,s1 in l:
            s.append((target-p)/s1)
            if len(s)>=2 and s[-1]<=s[-2]:
                s.pop()
        return len(s)
