class StockSpanner:

    def __init__(self):
        self.s=[]
        

    def next(self, price: int) -> int:
        k=[]
        count=1
        if not self.s:
            k.append(count)
            
        else:
            for i in self.s[::-1]:
                if i<=price:
                    count+=1
                else:
                    break
            k.append(count)
        self.s.append(price)
        count=max(k)


        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)