# leetcode 376 摆动序列

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        curDiff = 0  # 当前一对元素的差值
        preDiff = 0  # 前一对元素的差值
        result = 1  # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值）

        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1
                preDiff = curDiff

        return result



## 写一下动态规划怎么做

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        # 写一下动态规划

        dp = []

        for i in range(len(nums)):
            dp.append([1, 1])
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][1] = max(dp[j][0] + 1, dp[i][1])

                if nums[i] < nums[j]:
                    dp[i][0] = max(dp[j][1] + 1, dp[i][0])

        return max(dp[-1][0], dp[-1][1])