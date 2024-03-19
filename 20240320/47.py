# leetcode 47 全排列 II


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backTracking([], result, [False] * len(nums), nums)
        return result

    def backTracking(self, path, result, used, nums):
        if len(nums) == len(path):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]) or used[i]:
                continue

            path.append(nums[i])
            used[i] = True

            self.backTracking(path, result, used, nums)

            path.pop()
            used[i] = False