class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False

        reqSum = sum(nums)//k

        bucket = [0]*k
        nums.sort()
        def dfs(i):
            if i==len(nums):
                return True
            for j in range(k):
                if j>0 and bucket[j-1]==0:
                    continue
                if bucket[j]+nums[i]<=reqSum:
                    bucket[j]+=nums[i]
                    if dfs(i+1):
                        return True
                    bucket[j]-=nums[i]
            return False

        return dfs(0)
