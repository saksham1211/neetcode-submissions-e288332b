class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=r
        
        def isValid(mid):
            d=1
            total=0
            for w in weights:
                if total+w>mid:
                    d+=1
                    total=0

                total+=w
        
            return d<=days


        while l<=r:
            mid = (l+r)//2

            if isValid(mid):
                res=mid
                r=mid-1

            else:
                l=mid+1

        return res

