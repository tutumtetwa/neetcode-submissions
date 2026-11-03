class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        if not grid:
            return 0

        islands = 0

        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (0 <= nc < COLS and 0 <= nr < ROWS and grid[nr][nc] == '1'):
                        grid[nr][nc] = '0'
                        q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        return islands
        