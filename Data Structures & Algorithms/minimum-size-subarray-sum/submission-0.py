class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l=0
        r=0
        currSum=0
        res=float("inf")
        while r<len(nums):
            currSum+=nums[r]
            while currSum>=target:
                res=min(res, r-l+1)
                currSum-=nums[l]
                l+=1
            r+=1
                
        return res if res!=float("inf") else 0
