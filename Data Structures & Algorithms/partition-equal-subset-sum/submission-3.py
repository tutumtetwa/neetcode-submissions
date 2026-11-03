class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = set([0])

        # for i in range(len(nums) - 1, -1, -1):
        for i in range(len(nums)):
            NextDP = set()

            for t in dp:
                if t + nums[i] == target:
                    return True

                NextDP.add(t)
                NextDP.add(t + nums[i])
            dp = NextDP
        
        return False


        