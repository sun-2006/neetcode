class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming={}
        outgoing={}
        for i in trust:
            incoming[i[1]]=incoming.get(i[1],0)+1
            outgoing[i[0]]=outgoing.get(i[0],0)+1
        a=b=-1
        for i,j in incoming.items():
            if j==n-1:
                a=i
        if a not in outgoing:
            return a
        else:
            return -1
