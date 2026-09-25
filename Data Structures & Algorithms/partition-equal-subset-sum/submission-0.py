class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        set1={0}
        sum1=sum(nums)
        if sum1%2!=0:
            return False
        sum1=sum1//2
        for num in nums:
            set2=set(set1)
            for data in set1:
                current_data=data+num
                if current_data==sum1:
                    return True
                if current_data<sum1:
                    set2.add(current_data)
            set1=set2
        return sum1 in set1