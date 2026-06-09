class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Decide: start a new subarray or continue the existing one
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the global maximum
            max_so_far = max(max_so_far, current_sum)
            
        return max_so_far