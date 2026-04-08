class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        cols=len(grid[0])
        visit=set()
        maxarea=0

        def dfs(r, c):
            if r>=row or r<0:
                return 0

            if c>=cols or c<0:
                return 0

            if (r, c) in visit:
                return 0

            if grid[r][c]==0:
                return 0

            visit.add((r, c))
            area=1+dfs(r+1, c)+dfs(r-1, c)+dfs(r, c+1)+dfs(r, c-1)

            return area

        for r in range(row):
            for c in range(cols):   
                maxarea=max(maxarea, dfs(r, c))
        return maxarea