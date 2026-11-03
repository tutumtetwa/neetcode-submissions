class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        lo = 0
        hi = m * n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            r, c = divmod(mid, n)

            val = matrix[r][c]

            if val == target:
                return True

            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False