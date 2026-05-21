class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visit=set()
        def dfs(r, c, index):
            if index==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols or (r, c) in visit:
                return False

            if board[r][c]==word[index]:
                visit.add((r,c))
                res = dfs(r+1, c, index+1) or dfs(r, c+1, index+1) or dfs(r-1, c, index+1) or dfs(r, c-1, index+1)
                visit.remove((r, c))
                return res
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    if dfs(r, c, 0):
                        return True

        return False


        