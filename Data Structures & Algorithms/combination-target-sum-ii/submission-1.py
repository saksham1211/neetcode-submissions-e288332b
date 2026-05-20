class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i, total, stack):
            if total == target:
                res.append(stack.copy())
                return

            if total>target:
                return

            if i==len(candidates):
                return
            

            stack.append(candidates[i])
            dfs(i+1, total+candidates[i], stack)
            stack.pop()
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1, total, stack)

        dfs(0, 0, [])
        return res