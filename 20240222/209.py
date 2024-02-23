# 209 长度最小的子数组


# 第一种方法是滑动窗口 双指针
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # 定义双指针
        left, right = 0, 0
        total = 0

        # 这个数要定义比数组大1 因为有可能全部数组都用来组成最小序列了
        ans = len(nums) + 1
        # 开始走循环 外层循环条件是快指针走到结束
        while right <= len(nums) - 1:
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return 0 if ans == len(nums) + 1 else ans