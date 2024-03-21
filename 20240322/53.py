# leetcode 53 最大子数组和

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        count = 0
        result = float('-Inf')

        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:
                count = 0

        return result

# 练习一下动态规划

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划的版本
        if len(nums) == 1:
            return nums[-1]

        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            result = max(dp[i], result)

        return result