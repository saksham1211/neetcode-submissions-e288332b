class Solution:
    def climbStairs(self, n: int) -> int:
        dic={}
        def dfs(i):
            if i in dic:
                return dic[i]

            if i==n:
                return 1

            if i>n:
                return 0

            dic[i]=dfs(i+1)+dfs(i+2)

            return dic[i]

        return dfs(0)