# leetcode 454 四数相加

# 首先就是哈希表 这道题的时间复杂度不可避免地需要n方

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 尝试手撸一下这个题目 主要思路还是用map

        # 首先定义一下字典
        ansAB = dict()
        ansCD = dict()

        n = 0
        # 首先计算一下数组的长度，因为n没给
        for i in nums1:
            n += 1

        for i in range(n):
            # 对ab组合处理
            for j in range(n):
                tmp = nums1[i] + nums2[j]
                # 这块的进阶写法一定要习惯
                ansAB[tmp] = ansAB.get(tmp, 0) + 1

            # 对cd组合处理CD
            for j in range(n):
                tmp = nums3[i] + nums4[j]
                ansCD[tmp] = ansCD.get(tmp, 0) + 1

        # 最终计数
        res = 0

        # 此时此刻的ansAB和ansCD的格式应该是{加和值：出现次数}
        for i in ansAB:
            if -i in ansCD:
                res += ansAB[i] * ansCD[-i]

        return res





