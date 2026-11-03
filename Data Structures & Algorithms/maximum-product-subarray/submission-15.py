class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        minc, maxc = 1, 1

        for n in nums:
            tmp = n * maxc
            maxc = max(maxc * n, minc * n, n)
            minc = min(tmp, minc * n, n)
            res = max(res, maxc, minc)
        
        return res
        