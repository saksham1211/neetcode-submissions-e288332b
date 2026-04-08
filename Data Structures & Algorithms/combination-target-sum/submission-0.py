class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        stack=[]
        def backtracking(i, total):
            if total==target:
                res.append(stack.copy())
                return
            if total>target:
                return 0
                
            if i>=len(nums):
                return 0

            stack.append(nums[i])
            backtracking(i, total+nums[i])
            stack.pop()
            backtracking(i+1, total)

            return res

        return backtracking(0, 0)

        

