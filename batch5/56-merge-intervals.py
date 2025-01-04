class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            # Not Overlapped.
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            
            # Overlapped.
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            
        return result
