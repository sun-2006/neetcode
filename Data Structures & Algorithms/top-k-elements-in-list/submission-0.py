class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            dict1=dict()
            for i in nums:
                if i not in dict1:
                    dict1[i]=1
                else:
                    dict1[i]+=1
            maxi=maxv=0
            l=[]
            for k1 in range(k):
                for i in dict1:
                    if maxv<dict1[i]:
                        maxv=dict1[i]
                        maxi=i
                dict1[maxi]=0
                l.append(maxi)
                maxi=maxv=0
            return l
