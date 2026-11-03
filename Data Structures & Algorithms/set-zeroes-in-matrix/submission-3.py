class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        for r in range(ROWS):
            for c in range(COLS):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
        

            
        
        