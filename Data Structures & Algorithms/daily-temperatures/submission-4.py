class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        result=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while s and s[-1][0]<t:
                stackT,stackInd=s.pop()
                result[stackInd]=i-stackInd
            s.append((t,i))
        return result

