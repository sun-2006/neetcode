class StockSpanner:

    def __init__(self):
        self.s=[]
        

    def next(self, price: int) -> int:
        k=[]
        count=1
        if not self.s:
            k.append(count)
            
        else:
            leng=len(self.s)
            while leng>0 and self.s[leng-1]<=price:
                count+=1
                leng-=1
            k.append(count)
        self.s.append(price)
        count=max(k)


        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)