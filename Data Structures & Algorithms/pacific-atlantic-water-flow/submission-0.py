class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        paci, atla = set(), set()
        
        def dfs(r, c, prevh, seen):
            if (r < 0 or c < 0 or c == COLS or r == ROWS or heights[r][c] < prevh or (r, c) in seen):
                return
            seen.add((r, c))
            dfs(r + 1, c, heights[r][c], seen)
            dfs(r - 1, c, heights[r][c], seen)
            dfs(r, c + 1, heights[r][c], seen)
            dfs(r, c - 1, heights[r][c], seen)

        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], paci)
            dfs(r, COLS - 1, heights[r][COLS - 1], atla)

        for c in range(COLS):
            dfs(0, c, heights[0][c], paci)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atla)
        
        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in paci and (r, c) in atla:
                    ans.append([r, c])
        return ans


        