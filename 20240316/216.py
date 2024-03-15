# leetcode 216 组合总和 III

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backTracking(k, n, 1, 0, [], result)
        return result

    def backTracking(self, k, n, startIndex, curSum, path, result):
        if curSum > n:
            return
        if len(path) == k:
            if curSum == n:
                result.append(path[:])
            return

        for i in range(startIndex, 9 - (k - len(path)) + 2):
            curSum += i
            path.append(i)
            self.backTracking(k, n, i + 1, curSum, path, result)
            curSum -= i
            path.pop()


