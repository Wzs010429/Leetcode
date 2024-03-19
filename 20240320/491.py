# leetcode 491 非递减子序列

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backTracking(nums, [], result, 0)
        return result

    def backTracking(self, nums, path, result, startIndex):
        if len(path) >= 2:
            result.append(path[:])

        used = set()

        for i in range(startIndex, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in used:
                continue
            used.add(nums[i])
            path.append(nums[i])

            self.backTracking(nums, path, result, i+1)
            path.pop()