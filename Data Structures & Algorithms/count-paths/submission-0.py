class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row = [1] * n
     
        for _ in range(m - 1):
            
            newrow = [1] * n
           
            for j in range(n - 2, -1, -1):
                print(newrow[j + 1])
                newrow[j] = newrow[j + 1] + row[j]
            row = newrow
            

        return row[0]

       