# leetcode 93 复原IP地址

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backTracking(s, "", result, 0, 1)
        return result

    def backTracking(self, s, path, result, startIndex, parts):
        if parts == 4:
            if self.isValidNum(s, startIndex, len(s) - 1):
                path += s[startIndex:]
                result.append(path[:])
            return

        for i in range(startIndex, len(s)):
            if self.isValidNum(s, startIndex, i):
                self.backTracking(s, path + s[startIndex:i + 1] + '.', result, i + 1, parts + 1)
            else:
                break

    def isValidNum(self, number, left, right):
        if left > right:
            return False
        if left < right and number[left] == '0':  # 如果数字以'0'开头且长度大于1，则无效
            return False
        if int(number[left:right + 1]) > 255:  # 如果数字大于255，则无效
            return False
        return True