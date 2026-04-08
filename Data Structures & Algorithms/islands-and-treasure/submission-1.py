class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return grid

        row=len(grid)
        cols=len(grid[0])

        q=deque()
        for r in range(row):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r, c))

        directions=[[0, 1], [1, 0], [-1, 0], [0, -1]]

        while q:
            r, c=q.popleft()
            for dr, dc in directions:
                nr, nc=r+dr, c+dc

                if 0<=nr<row and 0<=nc<cols and grid[nr][nc]==2147483647:
                    grid[nr][nc]=grid[r][c]+1

                    q.append((nr, nc))

  