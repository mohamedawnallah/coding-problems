class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        result = [points[0]]
        for i in range(1, len(points)):
            if points[i][0] <= result[-1][1]:
                result[-1][0] = max(result[-1][0], points[i][0])
                result[-1][1] = min(result[-1][1], points[i][1])
            else:
                result.append(points[i])

        return len(result)
