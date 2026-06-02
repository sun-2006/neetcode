class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num1=num2=-1
        l1=[]
        for i in range(len(numbers)):
            if(num1==-1):
                num1=target-numbers[i]
                if num1 in numbers and num1!=numbers[i]:
                    num2=i
                    continue
                else:
                    num1=-1
            else:
                if(numbers[i]==num1):
                    num1=i
                    break
                else:continue
        l1.append(num2+1)
        l1.append(num1+1)
        return l1


        