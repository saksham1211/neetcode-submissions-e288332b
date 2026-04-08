class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        stack=[]
        candidates.sort()
        def backtrack(i, total):
            if total==target:
                res.append(stack.copy())
                return

            if total>target:
                return 0

            if i>=len(candidates):
                return 0

            stack.append(candidates[i])
            backtrack(i+1, total+candidates[i])
            stack.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1, total)

        backtrack(0, 0)
        return res