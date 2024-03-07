# leetcode 559 N叉树的最大深度

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

## 第一种 递归法
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        depth = 1

        for i in root.children:
            depth = max(depth, self.maxDepth(i) + 1)

        return depth


## 第二种 使用队列的层序遍历

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        queue = collections.deque([root])

        depth = 0
        while queue:
            queueLen = len(queue)

            for _ in range(queueLen):
                node = queue.popleft()
                for i in node.children:
                    queue.append(i)

            depth += 1

        return depth



## 迭代法 但是用栈

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # 使用栈的迭代法

        # 我算是看明白了 栈这种数据结构你就得 只能带着层数往栈里存

        if not root:
            return 0

        stack = [(root, 1)]
        depth = 1
        while stack:
            node, depthL = stack.pop()
            depth = max(depthL, depth)
            for i in node.children:
                stack.append((i, depthL + 1))

        return depth
