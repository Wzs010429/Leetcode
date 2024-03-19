# leetcode 46 全排列

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backTracking(nums, result, [], [False] * len(nums))
        return result

    def backTracking(self, nums, result, path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.backTracking(nums, result, path, used)
            path.pop()
            used[i] = False
