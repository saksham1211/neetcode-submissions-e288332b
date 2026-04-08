class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        visit=set()
        def dfs(r, c, i):
            if i==len(word):
                return True


            if r>=row or r<0:
                return False
            if c>=col or c<0:
                return False

            if (r, c) in visit:
                return

            if board[r][c]!=word[i]:
                return False
            visit.add((r, c))
            res= (
                dfs(r+1, c, i+1)or
                dfs(r, c+1, i+1)or
                dfs(r-1, c, i+1)or
                dfs(r, c-1, i+1)
            )
            visit.remove((r, c))
            return res

        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    if dfs(i, j, 0):
                        return True

        return False