class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float('-inf')

        for i in range(len(nums)):
            print(nums[i])
            ans = nums[i]
            res = max(res , ans)
            for j in range(i + 1, len(nums)):
                ans *= nums[j]
                res = max(res, ans)
        
        return res
        