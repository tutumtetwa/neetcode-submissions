class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        def addcells(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == -1 or (r, c) in seen):
                return
            
            q.append((r, c))
            seen.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    seen.add((r, c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addcells(r + 1, c)
                addcells(r - 1, c)
                addcells(r, c - 1)
                addcells(r, c + 1)
            dist += 1
        

        