# leetcode 239 滑动窗口的最大值

from collections import deque

class Myqueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def maxVal(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # 定义一个单项队列
        queue = Myqueue()
        # 定义一个结果数组
        res = []

        # 把最开始的k个值放进数组中
        for i in range(k):
            queue.push(nums[i])
        # 找到最开始的k个值的最大值并且放到结果数组中
        res.append(queue.maxVal())

        for i in range(k, len(nums)):
            queue.pop(nums[i - k])
            queue.push(nums[i])
            res.append(queue.maxVal())

        return res