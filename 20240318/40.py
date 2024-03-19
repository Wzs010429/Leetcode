# leetcode 40 组合总和 II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()
        self.backTracking(candidates, target, [], result, 0)
        return result

    def backTracking(self, candidates, target, path, result, startIndex):
        if sum(path) > target:
            return

        if sum(path) == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue

            path.append(candidates[i])
            self.backTracking(candidates, target, path, result, i + 1)
            path.pop()
