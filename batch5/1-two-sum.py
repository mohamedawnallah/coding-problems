class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            if nums[i] in result:
                return [result[nums[i]], i]
            result[target-nums[i]] = i
        
        raise Exception("Expected exactly one solution")
