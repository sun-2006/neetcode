class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        mul=1
        count=0
        for i in nums:
            if(i!=0):
                mul*=i
            else:
                count+=1
        for i in nums:
            if(count==0):
                output.append(int(mul/i))
            elif count>1 or i!=0:
                output.append(0)
            elif count==1 and i==0:
                output.append(mul) 

        return output
        