# leetcode 738 单调递增的数字

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:

        n = str(n)
        index = len(n)

        for i in range(len(n) - 1, 0, -1):
            if n[i] < n[i - 1]:
                index = i
                n = n[:i - 1] + str(int(n[i - 1]) - 1) + n[i:]

        return int(n[:index] + '9' * (len(n) - index))