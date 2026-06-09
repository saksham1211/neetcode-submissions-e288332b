class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        
        res=0

        def isValid(mid):
            time = 0
            for p in piles:
                time+=math.ceil(p/mid)

            return time<=h

        while l<=r:
            mid = (l+r)//2

            if isValid(mid):
                res=mid
                r=mid-1

            else:
                l=mid+1

        return res

            
        