# leetcode 104 二叉树的最大深度

# 第一种方法 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # 这是递归法

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

# 方法二 层序遍历 迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # 用层序遍历的迭代法做一下

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = collections.deque([root])

        depth = 0
        while queue:
            queueLen = len(queue)

            for _ in range(queueLen):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth