# leetcode 39 组合总和


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.backTracking(candidates, target, 0, [], self.result)
        return self.result

    def backTracking(self, candidates, target, startIndex, path, result):
        if sum(path) > target:
            return

        if sum(path) == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            self.backTracking(candidates, target, i, path, result)
            path.pop()
