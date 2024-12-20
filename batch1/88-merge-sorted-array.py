class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        
        nums1[:j+1] = nums2[:j+1]

        # Time Complexity: O(n+m)
        # Space Complexity: O(1)

        # Brute Force: Time Complexity O(m+n log m+n)
        # Space Complexity: O(m+n)