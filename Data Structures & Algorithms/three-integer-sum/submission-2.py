class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i, n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue

            else:
                l=i+1
                r=len(nums)-1

                while l<r:
                    ans=n+nums[l]+nums[r]

                    if ans==0:
                        res.append([n, nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1

                    if ans>0:
                        r-=1
                    if ans<0:
                        l+=1

                    
        return res


