# 反转字符串中的单词

class Solution:
    def reverseWords(self, s: str) -> str:

        # 移除字符串前后的空格并分割单词
        words = s.strip()
        words = words[::-1]

        # 翻转单词列表
        reversed_words = [word[::-1] for word in words.split()]

        # 重新连接单词并返回
        return " ".join(reversed_words)



# 用双指针去做

class Solution:
    def reverseWords(self, s: str) -> str:
        # 将字符串拆分为单词，即转换成列表类型
        words = s.split()

        # 反转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换成字符串
        return " ".join(words)