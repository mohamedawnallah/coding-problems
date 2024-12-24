class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        current_sum, window_start = 0, 0
        for window_end in range(len(nums)):
            current_sum += nums[window_end]
            while current_sum >= target:
                min_len = min(min_len, window_end-window_start+1)
                current_sum -= nums[window_start]
                window_start += 1
        return min_len if min_len != float('inf') else 0
