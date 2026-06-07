class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1

        maxWater = 0
        while l<r:
            lh = heights[l]
            rh = heights[r]
            water = (r-l)*(min(lh, rh))

            maxWater = max(maxWater, water)

            if lh<=rh:
                l+=1
            else:
                r-=1

        return maxWater