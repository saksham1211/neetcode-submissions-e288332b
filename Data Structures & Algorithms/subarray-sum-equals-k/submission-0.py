class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        ans=0
        currSum = 0
        for n in nums:
            currSum+=n
            if currSum-k in prefix:
                ans+=prefix[currSum-k]

            prefix[currSum] = prefix.get(currSum, 0)+1

        return ans