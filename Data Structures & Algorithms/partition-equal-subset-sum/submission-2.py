class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            NextDP = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                NextDP.add(t + nums[i])
                NextDP.add(t)
            print(NextDP)
            dp = NextDP
        
        return False
        