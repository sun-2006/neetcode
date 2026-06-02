class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        minBuy=prices[0]
        for sales in prices:
            maxP=max(maxP,sales-minBuy)
            minBuy=min(minBuy,sales)
        return maxP