class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        def dfs(Nopen, Nclose, stack):
            if Nopen==Nclose==n:
                res.append("".join(stack.copy()))
                return

            if Nopen<n:
                stack.append("(")
                dfs(Nopen+1, Nclose, stack)
                stack.pop()

            if Nopen>Nclose:
                stack.append(")")
                dfs(Nopen, Nclose+1, stack)
                stack.pop()


        dfs(0, 0, [])
        return res