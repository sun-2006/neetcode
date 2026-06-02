class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=l2=0
        combine=""
        r1=len(word1)
        r2=len(word2)
        while(l1<r1 and l2<r2):
            combine+=(word1[l1]+word2[l2])
            l1+=1
            l2+=1
        while(l1<r1):
            combine+=word1[l1]
            l1+=1
        while l2<r2:
            combine+=word2[l2]
            l2+=1
        return combine



        