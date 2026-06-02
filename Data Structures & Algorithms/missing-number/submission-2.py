class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num=0
        for i in range(len(nums)):
            num=num^nums[i]
            num=num^i
        num=num^len(nums)
        return num
