# 704二分查找

# 左闭右开区间写法
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 首先判断是不是越界的target
        if target not in nums:
            return -1

        # 定义一个两个index 第一个是开头 第二个是结尾
        flag_left, flag_right = 0, len(nums)

        while flag_left < flag_right:
            # 定义中间值=左边指针偏移量+左右指针中间值
            value_index = flag_left + (flag_right - flag_left) // 2

            # 找到对应值
            if target == nums[value_index]:
                return value_index
            if target < nums[value_index]:
                flag_right = value_index
            if target > nums[value_index]:
                flag_left = value_index + 1

        return -1


# 左闭右闭区间写法
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 首先判断是不是越界的target
        if target not in nums:
            return -1

        # 定义一个两个index 第一个是开头 第二个是结尾
        flag_left, flag_right = 0, len(nums)-1

        while flag_left <= flag_right:
            # 定义中间值=左边指针偏移量+左右指针中间值
            value_index = flag_left + (flag_right - flag_left) // 2

            # 找到对应值
            if target == nums[value_index]:
                return value_index
            if target < nums[value_index]:
                flag_right = value_index - 1
            if target > nums[value_index]:
                flag_left = value_index + 1

        return -1