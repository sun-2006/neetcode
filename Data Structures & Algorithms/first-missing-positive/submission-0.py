class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums1=sorted(nums)
        num=nums1[-1]
        if(num<=0):
            num=1
        for i in range(1,num+2):
            if i not in nums:
                return i
        