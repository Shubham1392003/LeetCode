class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue = float('inf')
        maxprofit = 0
        for price in prices:
            minvalue = min(minvalue,price)
            maxprofit = max(maxprofit,price-minvalue)
        return maxprofit
        