class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        def addcell(r, c):
            nonlocal fresh
            if (r < 0 or c < 0 or c == COLS or r == ROWS or grid[r][c] != 1):
                return
            grid[r][c] = 2
            q.append((r, c))
            fresh -= 1
        
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addcell(r + 1, c)
                addcell(r - 1, c)
                addcell(r, c + 1)
                addcell(r, c - 1)
            time += 1
        
        return time if fresh == 0 else -1
                
