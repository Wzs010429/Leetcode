# leetcode 45 跳跃游戏 II

class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        curlen = 0
        nextlen = 0
        step = 0

        for i in range(len(nums)):
            nextlen = max(nextlen, i+nums[i])
            if i == curlen:
                step += 1
                curlen = nextlen
                if nextlen >= len(nums)-1:
                    return step