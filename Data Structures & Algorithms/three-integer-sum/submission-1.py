class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = a + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ans.append((a, nums[l], nums[r]))
                    # l += 1
                    # while nums[l] == nums[l -1]:
                    #     l += 1
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
        return ans

        