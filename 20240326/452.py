# leetcode 452 用最少数量的箭引爆气球

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[1])
        result = 1

        for i in range(len(points) - 1):
            if points[i][1] < points[i + 1][0]:
                result += 1
            else:
                points[i + 1][1] = points[i][1]

        return result