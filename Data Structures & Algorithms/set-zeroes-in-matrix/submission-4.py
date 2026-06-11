class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowset = set()
        colset = set()

        rows = len(matrix)
        cols  = len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowset.add(r)
                    colset.add(c)


        for r in rowset:
            for c in range(cols):
                matrix[r][c] = 0

        for c in colset:
            for r in range(rows):
                matrix[r][c]=0

                