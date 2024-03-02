# leetcode 150 逆波兰表达式求值


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operator = ['+', '-', '*', '/']

        for i in tokens:
            if i not in operator:
                stack.append(int(i))
            else:
                opt2 = stack.pop()
                opt1 = stack.pop()
                if i == '+':
                    res = opt1 + opt2
                elif i == '-':
                    res = opt1 - opt2
                elif i == '*':
                    res = opt1 * opt2
                elif i == '/':
                    res = int(opt1 / opt2)
                stack.append(res)

        return stack.pop()
