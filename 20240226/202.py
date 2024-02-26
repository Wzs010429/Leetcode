# leetcode 202 快乐数 easy

class Solution:
    def isHappy(self, n: int) -> bool:
        # 首先尝试用哈希表去做
        resSet = set()

        while True:
            # 计算当前轮次的值
            n = self.getSum(n)

            # 如果等于1 直接退出
            if n == 1:
                return True

            if n in resSet:
                return False
            else:
                resSet.add(n)


    def getSum(self, n: int):
        res = 0

        while n:
            # divmode 会返回一个n/10的整除的商和余数
            n, r = divmod(n, 10)
            res += r * r

        return res



## 然后是喜闻乐见的双指针秒了这道题目

class Solution:
    def isHappy(self, n: int) -> bool:
        # 双指针秒了这道题目
        # 首先定义双指针
        slow, quick = n, self.getSum(n)

        # 这块判断quick本身等于1的时候是因为如果quick等于1了那么后续无论走多少步骤都是1
        while quick != slow and quick != 1:
            slow = self.getSum(slow)
            quick = self.getSum(self.getSum(quick))

        return quick == 1

    def getSum(self, n: int):
        res = 0

        while n:
            # divmode 会返回一个n/10的整除的商和余数
            n, r = divmod(n, 10)
            res += r * r

        return res