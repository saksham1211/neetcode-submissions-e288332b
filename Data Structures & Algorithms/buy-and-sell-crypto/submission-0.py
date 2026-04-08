class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        profit=0
        max_profit=0

        while r<len(prices):
            while r<len(prices) and prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                max_profit=max(profit, max_profit)
                r+=1

            l=r
            r+=1

        return max_profit
