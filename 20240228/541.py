# leetcode 541 反转字符串 II

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        result = []

        for i in range(0, n, 2 * k):
            result.append(s[i:i + k][::-1] + s[i + k:i + 2 * k])

        return ''.join(result)
