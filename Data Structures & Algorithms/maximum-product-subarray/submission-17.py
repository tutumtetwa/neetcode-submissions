class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums:
            tmp = n * curr_max
            curr_max = max(tmp, curr_min * n, n)
            curr_min = min(tmp, curr_min * n, n)
            res = max(res, curr_max)

        return res
        