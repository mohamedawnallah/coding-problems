class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = Solution.compute_left_product(nums)
        right_product = Solution.compute_right_product(nums)
        return Solution.compute_product_except_self(left_product, right_product)

    @staticmethod
    def compute_product_except_self(left_product, right_product):
        for i in range(len(left_product)):
            left_product[i] *= right_product[i]
        return left_product

    @staticmethod
    def compute_left_product(nums):
        n = len(nums)
        left_product = [1] * n
        product = nums[0]
        for i in range(1, n):
            left_product[i] = product
            product *= nums[i]
        return left_product
    
    @staticmethod
    def compute_right_product(nums):
        n = len(nums)
        right_product = [1] * n
        product = nums[n-1]
        for i in range(n-2, -1, -1):
            right_product[i] = product
            product *= nums[i]
        return right_product
