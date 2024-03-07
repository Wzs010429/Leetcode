# leetcode 222 完全二叉树的节点个数


# 第一种 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 先用递归法去写
        return self.countNum(root)

    def countNum(self, node):
        if not node:
            return 0

        leftnum = self.countNum(node.left)
        rightnum = self.countNum(node.right)

        return leftnum + rightnum + 1


# 第二种方法 迭代法 先用的队列


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 用迭代法去写

        # 队列

        if not root:
            return 0
        num = 0
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            num += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return num

#  第三种方法 用栈


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 用迭代法去写

        # 用栈去写

        if not root:
            return 0
        num = 0
        stack = [root]

        while stack:
            node = stack.pop()
            num += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return num


## 完全二叉树的判定方式来做这个题目

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        # 用完全二叉树的思路去做
        if not root:
            return 0

        left = root.left
        right = root.right
        leftLen, rightLen = 1, 1

        while left:
            left = left.left
            leftLen += 1
        while right:
            right = right.right
            rightLen += 1

        if leftLen == rightLen:
            return (2 ** leftLen) - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1

