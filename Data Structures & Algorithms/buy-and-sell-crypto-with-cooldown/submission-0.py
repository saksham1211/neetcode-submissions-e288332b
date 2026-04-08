class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        hold=[0 for _ in range(n)]
        sell=[0 for _ in range(n)]
        cooldown=[0 for _ in range(n)]

        hold[0]=-prices[0]
        sell[0]=0
        cooldown[0]=0

        for i in range(1, n):
            hold[i]=max(hold[i-1], cooldown[i-1]-prices[i])
            sell[i]=hold[i-1]+prices[i]
            cooldown[i]=max(cooldown[i-1], sell[i-1])

        return max(cooldown[n-1], sell[n-1])
