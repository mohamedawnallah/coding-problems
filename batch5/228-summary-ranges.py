class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        ranges = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if nums[i-1] == nums[start]:
                    ranges.append(str(nums[start]))
                else:
                    ranges.append(str(nums[start]) + "->" + str(nums[i-1]))
                start = i
        
        if nums[-1] == nums[start]:
            ranges.append(str(nums[-1]))
        else:
            ranges.append(str(nums[start]) + "->" + str(nums[-1]))
        
        return ranges
