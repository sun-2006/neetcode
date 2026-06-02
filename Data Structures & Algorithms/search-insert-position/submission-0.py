class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin=0
        end=len(nums)-1
        res=len(nums)
        while begin<=end:
            mid=(begin+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                res=mid
                end=mid-1
            else:
                begin=mid+1
        return res