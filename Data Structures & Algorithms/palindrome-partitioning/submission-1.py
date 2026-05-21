class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        def dfs(index, stack):
            if index==len(s):
                res.append(stack.copy())
                return

            for i in range(index, len(s)):
                st = s[index:i+1]
                if is_valid(st):
                    stack.append(st)
                    dfs(i+1, stack)
                    stack.pop()

        
        def is_valid(s):
            l=0
            r=len(s)-1

            while l<=r:
                if s[l]!=s[r]:
                    return False

                l+=1
                r-=1

            return True

        dfs(0, [])
        return res