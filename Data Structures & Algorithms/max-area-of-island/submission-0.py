class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            #if grid[r][c] == 0 or r not in range(ROWS) or c not in range(COLS) or (r, c) in visit:
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            visit.add((r, c))

            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))

        return area

                
        