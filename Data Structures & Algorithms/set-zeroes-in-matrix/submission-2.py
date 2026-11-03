class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # 1. Find all rows and cols with zeros
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # 2. Set rows and cols to zero
        for r in range(ROWS):
            for c in range(COLS):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

         

        

            
        
        