# Leetcode 459 重复的子字符串

# 第一种方法 使用KMP去做

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 首先把模式串的next数组构建出来
        nextlist = self.getNext(s)

        # 定义在主串和模式串中遍历的双指针
        i, j = 1, 0

        # 这个是合成的匹配串
        ss = s+s
        while i < len(ss)-1:
            # 模式串和主串的字符判定一致了就继续挪指针
            if ss[i] == s[j]:
                i += 1
                j += 1
            elif j > 0:
                j = nextlist[j - 1]
            else:
                i += 1

            if j == len(s):
                return True

        return False


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


# 第二种方法 适用py的内置函数 find 返回匹配索引的第一个下标
# 一行代码直接秒了 确实爽到爆炸
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        return True if (s+s).find(s, 1)!= len(s) else False


