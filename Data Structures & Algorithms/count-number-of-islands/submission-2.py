class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        cols=len(grid[0])
        islands=0
        visit=set()

        if not grid or not grid[0]:
            return 0

        def dfs(r, c):
            if r>=row or r<0:
                return

            if c>=cols or c<0:
                return

            if (r, c) in visit:
                return 

            if grid[r][c]=="0":
                return

            visit.add((r, c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(row):
            for c in range(cols):
                if grid[r][c] =="1" and (r, c) not in visit:
                    islands +=1
                    dfs(r,c)

        return islands

                