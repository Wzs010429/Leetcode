# 18 四数之和 medium

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 这道题目的核心思想还是通过双指针来解决实际问题
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):

            if nums[i] > target and target > 0:
                return result
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, n):
                if nums[i] + nums[j] > target and target > 0:
                    break

                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    res = nums[i] + nums[j] + nums[left] + nums[right]
                    if res > target:
                        right -= 1
                    elif res < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1

        return result
