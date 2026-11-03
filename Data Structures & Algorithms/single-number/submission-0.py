class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        Count = Counter(nums)
        for key, val in Count.items():
            if val == 1:
                return key
        