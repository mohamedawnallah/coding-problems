class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1
        
        return slow+1
