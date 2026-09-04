class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        l=[-1]*n
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        l[0]=nums[0]
        l[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            l[i]=max(l[i-1],nums[i]+l[i-2])
        return l[-1]
            