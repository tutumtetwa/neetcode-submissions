class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        def addcell(r, c):
            if (r < 0 or r == len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] != 1):
                return
            grid[r][c] = 2
            q.append((r, c))
            nonlocal fresh
            fresh -= 1

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                addcell(r + 1, c)
                addcell(r - 1, c)
                addcell(r, c + 1)
                addcell(r, c - 1)
            time += 1
        return time if fresh == 0 else -1