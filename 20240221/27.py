# 27.移除元素

# 首先是双指针方法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 定义慢指针
        num = 0
        # 这里面的i就是快指针
        for i in nums:
            # 对所有不等于val的值全部重新赋值更新数组
            if i != val:
                nums[num] = i
                num += 1
        return num


# 双指针优化方法
# 这种方法就是避免不等于val的nums中的元素重新赋值
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 定义出来左右指针，没有越界指针
        left = 0
        right = len(nums) - 1
        while(left <= right):
            # 将右指针的值更新在左指针进行不满足条件的值的替换，并且需要判断更新后的值是否满足条件
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left