class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_water=0

        while l<r:
            lh=heights[l]
            rh=heights[r]

            max_water=max(max_water, (min(lh, rh))*(r-l))
            
            if lh>rh:
                while rh>=heights[r] and l<r:
                    r-=1
            else:
                while lh>=heights[l] and l<r:
                    l+=1


        return max_water


