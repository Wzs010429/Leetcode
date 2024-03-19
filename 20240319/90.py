# leetcode 90 子集 II


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backTracking(nums, [], 0, result)

        return result

    def backTracking(self, nums, path, startIndex, result):
        result.append(path[:])

        for i in range(startIndex, len(nums)):

            if i > startIndex and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backTracking(nums, path, i + 1, result)
            path.pop()