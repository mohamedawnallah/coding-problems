class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = k % n

        # Reverse numbers.
        Solution.reverse(nums, 0, n-1)

        # Reverse first k numbers.
        Solution.reverse(nums, 0, k-1)

        # Reverse last k numbers.
        Solution.reverse(nums, k, n-1)

        
    @staticmethod
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1  
