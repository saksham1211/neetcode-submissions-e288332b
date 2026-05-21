class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]

        def dfs(index, stack):
            if index == len(s):
                res.append(" ".join(stack.copy()))
                return

            for i in range(index, len(s)):
                word = s[index:i+1]
                if word in wordDict:
                    stack.append(word)
                    dfs(i+1, stack)
                    stack.pop()

        dfs(0, [])
        return res