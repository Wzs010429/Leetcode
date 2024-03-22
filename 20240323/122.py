# leetcode 122 买股票的最佳时机 II

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 写一个贪心
        result = 0
        for i in range(len(prices)-1):
            tmp = prices[i+1] - prices[i]
            if tmp > 0:
                result += tmp

        return result

