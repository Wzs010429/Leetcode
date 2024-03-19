# leetcode 78 子集

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backTracking(nums, [], result, 0)
        return result

    def backTracking(self, nums, path, result, startIndex):
        result.append(path[:])

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backTracking(nums, path, result, i + 1)
            path.pop()
