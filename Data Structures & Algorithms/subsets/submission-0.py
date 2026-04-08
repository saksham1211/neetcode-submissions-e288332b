class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[]

        def backtracking(i):
            if i==len(nums):
                res.append(stack.copy())
                return

            stack.append(nums[i])
            backtracking(i+1)
            stack.pop()
            backtracking(i+1)
            return res

        return backtracking(0)


            