class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, max_so_far = 0, nums[0]
        cur_min, min_so_far = 0, nums[0]
        total_sum = 0
        
        for x in nums:
            # Standard Kadane's for Maximum
            cur_max = max(x, cur_max + x)
            max_so_far = max(max_so_far, cur_max)
            
            # Inverse Kadane's for Minimum
            cur_min = min(x, cur_min + x)
            min_so_far = min(min_so_far, cur_min)
            
            total_sum += x
            
        # If all numbers are negative, max_so_far is the best we can do
        if max_so_far < 0:
            return max_so_far
            
        return max(max_so_far, total_sum - min_so_far)