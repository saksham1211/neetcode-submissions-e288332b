class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
                
            skip = dfs(i+1)
            take = nums[i]+dfs(i+2)

            dp[i]=max(skip, take)

            return dp[i]

        return max(dfs(0), dfs(1))