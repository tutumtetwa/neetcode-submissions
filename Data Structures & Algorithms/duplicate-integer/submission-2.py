class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for i in range(len(nums)):
            if nums[i] in numset:
                return True
            numset.add(nums[i])
        return False   
        

        