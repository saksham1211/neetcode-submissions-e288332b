class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        length=0
        longest=0

        for n in nums:
            if (n-1) not in num_set:
                length=1
                while (n+1) in num_set:
                    length+=1
                    n=n+1
               

            longest=max(longest, length)

        return longest


