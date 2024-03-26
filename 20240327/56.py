# leetcode 56 合并区间

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result = []

        intervals.sort(key=lambda x: x[0])

        result.append(intervals[0])

        for i in range(len(intervals) - 1):
            if result[-1][1] >= intervals[i + 1][0]:
                result[-1][1] = max(intervals[i + 1][1], result[-1][1])
            else:
                result.append(intervals[i + 1])

        return result

