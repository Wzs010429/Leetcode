# Leetcode 28 找出字符串中第一个匹配项的下标

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # 首先把模式串的next数组构建出来
        nextlist = self.getNext(needle)

        # 定义在主串和模式串中遍历的双指针
        i, j = 0, 0

        while i < len(haystack):
            # 模式串和主串的字符判定一致了就继续挪指针
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = nextlist[j - 1]
            else:
                i += 1

            if j == len(needle):
                index = i - j
                return index

        return -1

    def getNext(self, numlist):

        # 定义一个要输出的数组 这个数组的第一位肯定是0
        nextlist = [0]
        nextprefix = 0  # 当前已经有多少个相同前后缀的长度

        i = 1
        while i < len(numlist):
            if numlist[nextprefix] == numlist[i]:
                nextprefix += 1
                nextlist.append(nextprefix)
                i += 1
            else:
                if nextprefix == 0:
                    nextlist.append(nextprefix)
                    i += 1
                else:
                    nextprefix = nextlist[nextprefix - 1]

        return nextlist





