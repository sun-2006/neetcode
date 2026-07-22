class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,total,l):
            if target==total:
                res.append(l.copy())
                return
            if total>target or i>=len(candidates):
                return
            l.append(candidates[i])
            dfs(i+1,total+candidates[i],l)
            l.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,total,l)
        dfs(0,0,[])
        return res