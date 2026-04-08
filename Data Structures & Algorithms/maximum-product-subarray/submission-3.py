class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        currMin, currMax=1, 1

        for n in nums:
            temp=currMax*n
            currMax=max(n*currMax, n*currMin, n)
            currMin=min(temp, n*currMin, n)

            res=max(currMax, res)

        return res


