# leectode 1047 删除字符串中的所有相邻重复项

# 这题蛮简单的 直接秒了

class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)
