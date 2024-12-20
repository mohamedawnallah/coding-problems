class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        for i in range(len(nums)):
            if i > jumps:
                return False
            jumps = max(jumps, nums[i]+i)

        return True
