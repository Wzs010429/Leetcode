# leetcode 131 分割回文串

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backTracing(s, 0, [], result)
        return result

    def backTracing(self, s, startIndex, path, result):
        if startIndex == len(s):
            result.append(path[:])
            return

        for i in range(startIndex, len(s)):
            if self.isPalidrome(s, startIndex, i):
                path.append(s[startIndex:i + 1])
                self.backTracing(s, i + 1, path, result)
                path.pop()

    def isPalidrome(self, str, left, right):
        left = left
        right = right

        while left < right:
            if str[left] == str[right]:
                left += 1
                right -= 1
            else:
                return False

        return True