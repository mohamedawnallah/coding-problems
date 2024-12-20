class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, count = 1, 1
        for fast in range(1, len(nums)):
            # If it is non duplicate based on last slow element or duplicates within range 2.
            if nums[fast] != nums[slow-1] or count < 2:
                nums[slow] = nums[fast]
                if nums[fast] == nums[slow-1]:
                    count += 1
                else:
                    count = 1
                slow += 1

        return slow
