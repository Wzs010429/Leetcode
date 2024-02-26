# leetcode 1 两数之和 easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 哈希表去check target-X是否存在
        hashSet = dict()

        # i是迭代值0123 j是nums对应i坐标下的值
        for i, j in enumerate(nums):
            if target - j in hashSet:
                # 返回的列表格式应该是已经存入hashSet的键值和新检索到的键值
                return [hashSet[target - j], i]
            # 存入格式是： 自身值：坐标
            hashSet[j] = i





