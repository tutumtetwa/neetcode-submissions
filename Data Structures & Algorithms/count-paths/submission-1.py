class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ROWS = m
        COLS = n

        row = [1] * COLS

        for _ in range(ROWS - 1):
            newrow = [1] * COLS
            for j in range(COLS - 2, -1, -1):
                newrow[j] = newrow[j + 1] + row[j]
            row = newrow
        
        return row[0]

       