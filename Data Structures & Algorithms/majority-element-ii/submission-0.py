class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l1=[]
        dict1={}
        for i in nums:
            if (i not in dict1):
                dict1[i]=1
            else:
                dict1[i]+=1
        print(dict1)
        for key,value in dict1.items():
            if (value>int((len(nums)//3))):
                l1.append(key)
        return l1
        