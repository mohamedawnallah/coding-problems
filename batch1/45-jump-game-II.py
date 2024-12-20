class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, local_max_jumps, global_max_jumps = 0, 0, 0
        for i in range(len(nums)-1):
            global_max_jumps = max(global_max_jumps, nums[i]+i)
            if local_max_jumps == i:
                local_max_jumps = global_max_jumps
                jumps += 1
        return jumps
