class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1=sorted(nums)
        count=1
        max=1
        if len(nums)==0:
            return 0
        for i in range(len(nums1)):
            if (i!=0):
                if((nums1[i-1]+1)==nums1[i] ):
                    count+=1
                elif (nums1[i-1])==nums1[i]:
                    continue
                else:
                    if (max<count):
                        max=count
                    count=1
        if(max<count):
            max=count

        return max
        