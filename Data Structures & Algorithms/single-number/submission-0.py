class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## XOR - a^a = 0 and a^0 = a

        res=0
        for n in nums:
            res = res^n

        return res