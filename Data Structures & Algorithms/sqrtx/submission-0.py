class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=x

        while l<=r:
            mid = (l+r)//2

            sqrt = mid*mid
            if sqrt==x:
                return mid

            elif sqrt>x:
                r=mid-1

            else:
                l=mid+1

        return r