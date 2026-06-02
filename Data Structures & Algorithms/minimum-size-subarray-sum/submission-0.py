class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength=len(nums)+1
        l=0
        sum1=0
        for r in range(len(nums)):
            sum1+=nums[r]
            if sum1>=target:
                minLength=min(minLength,r-l+1)
                sum1-=nums[l]
                l+=1
                while l!=r and sum1>=target :
                    minLength=min(minLength,r-l+1)
                    sum1-=nums[l]
                    l+=1
                    
        if sum1>=target:
            minLength=min(minLength,len(nums)-l)
        if minLength==len(nums)+1:
            return 0
        return minLength


