# leetcode 455 分发饼干

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # 这个是从小的饼干开始满足小孩儿
        g.sort()  # 孩子的胃口
        s.sort()  # 饼干的大小
        index = 0
        for i in range(len(s)):
            if index < len(g) and g[index] <= s[i]:
                index += 1

        return index


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # 这个是从大的饼干开始降维打击小孩儿
        g.sort()  # 孩子的胃口
        s.sort()  # 饼干的大小
        index = len(s) - 1
        result = 0
        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and g[i] <= s[index]:
                index -= 1
                result += 1

        return result