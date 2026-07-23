class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def backtrack(i,l):
            if i==len(nums):
                res.append(l.copy())
                return
            
            #you can take

            l.append(nums[i])
            i=i+1
            
            backtrack(i,l)
            l.pop()
            while i!=len(nums) and nums[i]==nums[i-1]:
                i=i+1
            backtrack(i,l)
        backtrack(0,[])
        return res
