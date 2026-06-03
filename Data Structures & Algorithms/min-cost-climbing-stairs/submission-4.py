class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0]*(len(cost)+1)
        for i in range(len(dp)-2, -1, -1):
            if i+2<len(dp):
                dp[i] = cost[i]+min(dp[i+1], dp[i+2])
            else:
                dp[i] = cost[i] + min(dp[i+1], 0)

        return min(dp[0], dp[1])