class Solution:
    def climbStairs(self, n: int) -> int:
        cache=[-1]*n
        def num(i):
            if i==n:
                return 1
            if i>n:
                return 0
            if cache[i]!=-1:
                return cache[i]
            cache[i]=num(i+1)+num(i+2)
            return cache[i]
        return num(0)