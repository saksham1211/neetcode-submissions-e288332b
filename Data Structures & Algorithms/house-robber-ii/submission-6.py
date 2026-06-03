class Solution:
    def maxRob(self, nums):
        dp={}
        def dfs(i):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]

            skip = dfs(i+1)
            take = nums[i]+dfs(i+2)
            dp[i] = max(skip, take)

            return dp[i]
        return max(dfs(0), dfs(1))

    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.maxRob(nums[1:]), self.maxRob(nums[:-1]))
        