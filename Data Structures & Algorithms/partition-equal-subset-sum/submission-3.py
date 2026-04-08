class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        target=sum(nums)//2
        dp=set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            nextdp=set()
            for t in dp:
                if (t+nums[i])==target:
                    return True

                nextdp.add(t+nums[i])
                nextdp.add(t)

            dp=nextdp

        return False