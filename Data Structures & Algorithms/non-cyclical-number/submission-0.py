class Solution:
    def isHappy(self, n: int) -> bool:
        def splitsumsqua(n):
            k=0
            while n>0:
                k+=(n%10)**2
                n=int(n/10)
            return k
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = splitsumsqua(n)

        return True