class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)

        # Pass 1: Add intervals that come before the new interval.
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        # Pass 2: Merge intervals that overlaps with the new interval if any.
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
        result.append(new_interval)

        # Pass 3: Add intervals that come after the new interval.
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
