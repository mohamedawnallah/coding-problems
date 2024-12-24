class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.search_pair(nums, -nums[i], i+1, triplets)
        return triplets
    
    def search_pair(self, nums, target_sum, left, triplets):
        right = len(nums)-1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, nums[left], nums[right]])
                left, right = left + 1, right - 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif current_sum > target_sum:
                right -= 1
            else:
                left += 1
