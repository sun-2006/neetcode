class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=nums[0]
        for i in nums:
            if(num<i):
                num=i
        if(num<=0):
            num=1
        for i in range(1,num+2):
            if i not in nums:
                return i