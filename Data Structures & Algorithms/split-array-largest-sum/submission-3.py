class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        res=r

        def isValid(mid):
            part = 1
            total=0
            for n in nums:
                if total+n>mid:
                    part+=1
                    total=0
                total+=n

            return part<=k

        while l<=r:
            mid = (l+r)//2

            if isValid(mid):
                res=mid
                r=mid-1

            else:
                l=mid+1

        return res