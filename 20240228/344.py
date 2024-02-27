# leetcode 344 字符串反转

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # 双指针秒了
        left, right = 0, len(s) - 1

        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp

            left += 1
            right -= 1


# 考虑用栈去解决

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 定义一个栈
        slack = []

        for i in s:
            slack.append(i)
        for i in range(len(slack)):
            s[i] = slack.pop()