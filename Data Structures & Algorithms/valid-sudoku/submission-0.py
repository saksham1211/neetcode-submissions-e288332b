class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square=defaultdict(set)
        colset = defaultdict(set)
        row = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==".":
                    continue

                else:
                    if board[r][c] in row[r] or board[r][c] in colset[c] or board[r][c] in square[(r//3, c//3)]:
                        return False


                val = board[r][c]
                row[r].add(val)
                colset[c].add(val)
                square[(r//3, c//3)].add(val)

        return True
