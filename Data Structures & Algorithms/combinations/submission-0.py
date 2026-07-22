class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]

        def dfs(i,l):
            if len(l)==k:
                res.append(l.copy())
                return
            if i>n:
                return
            l.append(i)
            dfs(i+1,l)
            l.pop()
            dfs(i+1,l)
        dfs(1,[])
        return res