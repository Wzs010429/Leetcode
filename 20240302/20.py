## leetcode 20 有效的括号

## 第一种方法尝试用栈的思想去做 但是栈的定义是一个列表

class Solution:
    def isValid(self, s: str) -> bool:

        # 创建一个判定的栈
        stack = []

        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            # 栈空了 说明字符少了
            # 或者是字符没对上
            elif not stack or i != stack[-1]:
                return False
            else:
                stack.pop()

        return True if not stack else False


# 做了一个映射表进来 就是一个字典 本质上这两种解法没有什么区别

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dic = {"(": ")", "{": "}", "[": "]"}

        for i in s:
            if i in dic.keys():
                stack.append(dic[i])
            elif not stack or stack[-1] != i:
                return False
            else:
                stack.pop()

        return True if not stack else False
