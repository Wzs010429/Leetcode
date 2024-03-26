# leetcode 435 无重叠区间

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        Overlap = 0

        intervals.sort(key=lambda x: x[1])

        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                Overlap += 1
                intervals[i+1][1] = intervals[i][1]

        return Overlap
