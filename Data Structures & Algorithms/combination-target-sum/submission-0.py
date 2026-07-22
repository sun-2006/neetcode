class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,total,l):
            if total==target:
                res.append(l.copy())
                return 
            if i>=len(nums) or total>target:
                return
            
            l.append(nums[i])
            dfs(i,total+nums[i],l)
            l.pop()
            dfs(i+1,total,l)
        dfs(0,0,[])
        return res