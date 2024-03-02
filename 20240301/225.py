# Leetcode 225 用队列实现栈

from collections import deque


class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())

        res = self.queue_in.pop()

        # 一种写法是直接给他两个队列互换
        # self.queue_in, self.queue_out = self.queue_out, self.queue_in

        for i in range(len(self.queue_out)):
            self.queue_in.append(self.queue_out.popleft())

        return res

    def top(self) -> int:
        if self.empty():
            return None

        res = self.queue_in.pop()
        self.queue_in.append(res)

        return res

    def empty(self) -> bool:
        return not self.queue_in

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()