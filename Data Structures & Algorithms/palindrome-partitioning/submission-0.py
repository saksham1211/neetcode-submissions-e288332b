class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        stack=[]
        def pali(s):
            return s==s[::-1]

        def backtrack(i, stack):
            if i==len(s):
                res.append(stack.copy())
                return

            for j in range(i+1, len(s)+1):
                substring=s[i:j]

                if pali(substring):
                    stack.append(substring)
                    backtrack(j, stack)
                    stack.pop()

        backtrack(0, [])
        return res