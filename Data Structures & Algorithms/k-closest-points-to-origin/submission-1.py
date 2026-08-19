class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[[((i[0]**2+i[1]**2)**0.5),i[0],i[1]] for i in points]
        heapq.heapify(l)
        res=[]
        while k>0:
            dist,x,y=heapq.heappop(l)
            res.append([x,y])
            k-=1
        return res

