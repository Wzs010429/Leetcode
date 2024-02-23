# Leetcode 977 有序数组的平方

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 双指针左右比较 因为最大值都出现在两边 nums是排了序的
        left, right = 0, len(nums) - 1
        flag = len(nums) - 1
        numList = [0] * len(nums)
        # 判断出来左右指针哪一个数值更大 往新的数组里面插入就可以了

        while left <= right:
            if nums[left]*nums[left] >= nums[right]*nums[right]:
                numList[flag] = nums[left]*nums[left]
                left += 1
            else:
                numList[flag] = nums[right]*nums[right]
                right -= 1
            flag -= 1
        return numList


# 下面的版本是重新练习快速排序
class Solution:
    # 正好利用这道题目重新练习一下快排
    def quickSort(self, nums, left, right):
        if left >= right:
            return
        pivot = left
        l, r = left, right
        while l < r:
            while l < r and nums[r] >= nums[pivot]:
                r -= 1
            while l < r and nums[l] <= nums[pivot]:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
        # 交换基准到正确的位置
        nums[left], nums[l] = nums[l], nums[left]

        self.quickSort(nums, left, l - 1)
        self.quickSort(nums, l + 1, right)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
