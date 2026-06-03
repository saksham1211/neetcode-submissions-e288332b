class Solution:
    def numDecodings(self, s: str) -> int:
        res=0
        dp={}
        def dfs(i):
            nonlocal res
            if i>=len(s):
                return 1
            if i in dp:
                return dp[i]


            if s[i]=="0":
                return 0

            if 1<=int(s[i])<=26:
                res = dfs(i+1)
                if i+1<len(s) and 9<int(s[i:i+2])<=26:
                    res+=dfs(i+2)
            dp[i]=res
            
            return dp[i]

        return dfs(0)
