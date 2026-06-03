class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(i, currSum):
            if currSum==amount:
                return 0

            if currSum>amount:
                return float("inf")

            if i>=len(coins):
                return float("inf")
            if (i, currSum) in dp:
                return dp[(i, currSum)]

            take = 1+dfs(i, currSum+coins[i])
            skip = dfs(i+1, currSum)

            dp[(i, currSum)] =  min(skip, take)
            return dp[(i, currSum)]

        ans = dfs(0, 0)
        return ans if ans!=float("inf") else -1