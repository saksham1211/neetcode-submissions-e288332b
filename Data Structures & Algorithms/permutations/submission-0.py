class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[]

        def backtracking(path, remaining):
            if not remaining:
                res.append(path)
                return

            for i in range(len(remaining)):
                backtracking(path+[remaining[i]], remaining[:i]+remaining[i+1:])

        backtracking([], nums)
        return res