# Leetcode 242 有效的字母异位词

# 这道题就用哈希表的方法去做

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # 定义两个哈希列表来统计每一个字母出现的个数
        # 一共就26个字母所以长度26就可以了
        numListS = [0] * 26
        numListT = [0] * 26

        # ord函数：它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
        for i in s:
            numListS[ord(i) - ord('a')] += 1

        for i in t:
            numListT[ord(i) - ord('a')] += 1

        return numListS == numListT