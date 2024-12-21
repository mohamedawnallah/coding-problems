class Solution:
    def trap(self, heights: List[int]) -> int:
        trapped_water = 0
        left, right = 0, len(heights)-1
        left_max, right_max = heights[left], heights[right]
        while left < right:
            if heights[left] < heights[right]:
                left += 1
                left_max = max(left_max, heights[left])
                trapped_water += left_max - heights[left]
            else:
                right -= 1
                right_max = max(right_max, heights[right])
                trapped_water += right_max - heights[right]
        return trapped_water
