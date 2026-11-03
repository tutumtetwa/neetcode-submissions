class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in twosum:
                return [twosum[diff], i]
            twosum[n] = i

        