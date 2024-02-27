# leetcode 15 三数之和

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 首先定义输出的结果数组
        res = []

        # 将数组进行从小到大的排序
        nums.sort()

        for i in range(len(nums)):
            # 如果排好序的第一个元素就是大于0的 那么就不用玩了
            if nums[i] > 0:
                return res

            # 判断i的前一个值和后面是不是一致的
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a1 = nums[i]
            # 定义左右双指针
            left, right = i + 1, len(nums) - 1

            while left < right:
                a2, a3 = nums[left], nums[right]

                ressum = a1 + a2 + a3
                if ressum > 0:
                    right -= 1

                elif ressum < 0:
                    left += 1

                else:
                    res.append([a1, a2, a3])

                    # 去重
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1

                    left += 1
                    right -= 1

        return res
