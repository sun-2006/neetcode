class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict1=dict()
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in dict1:
            if dict1[i]>1:
                return i