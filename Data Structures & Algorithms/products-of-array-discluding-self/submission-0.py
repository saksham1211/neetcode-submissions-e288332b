class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1 for i in range(len(nums))]
        right=[1 for i in range(len(nums))]
        res=[1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            left[i]=left[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right[i]=right[i+1]*nums[i+1]

        for i in range(len(left)):
            res[i]=left[i]*right[i]
        print(left)
        print(right)
        
        

        return res