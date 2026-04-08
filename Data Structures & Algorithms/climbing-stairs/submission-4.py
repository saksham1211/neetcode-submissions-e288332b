class Solution:
    def climbStairs(self, n: int) -> int:
        dic={}
        def dfs(steps):
            if steps==n:
                return 1

            if steps>n:
                return 0

            if steps in dic:
                return dic[steps]

            dic[steps]=dfs(steps+1)+dfs(steps+2)

            return dic[steps]

        return dfs(0)