# leetcode 101 对称二叉树


## 方法一 递归法


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # 自己尝试一下递归法
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.compare(root.left, root.right)

    def compare(self, left, right):

        if left is None and right is not None:
            return False
        elif right is None and left is not None:
            return False
        elif left is None and right is None:
            return True
        elif left.val != right.val:
            return False

        innerSide = self.compare(left.right, right.left)
        outerSide = self.compare(left.left, right.right)

        return innerSide and outerSide


## 方法二 迭代法 用队列

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        ## 迭代法 用队列

        if not root:
            return True

        stack = collections.deque()
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            left = stack.popleft()
            right = stack.popleft()

            if left is None and right is None:
                continue

            if left is None and right is not None:
                return False
            elif left is not None and right is None:
                return False
            elif left.val != right.val:
                return False

            # 添加左侧左子树和右侧右子树 外圈
            stack.append(left.left)
            stack.append(right.right)

            stack.append(left.right)
            stack.append(right.left)

        return True


## 方法三 迭代法 用栈
## 这个就是简单改了一小下 很简单和队列几乎没区别

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        ## 迭代法 用栈

        if not root:
            return True

        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            left = stack.pop()
            right = stack.pop()

            if left is None and right is None:
                continue

            if left is None and right is not None:
                return False
            elif left is not None and right is None:
                return False
            elif left.val != right.val:
                return False

            # 添加左侧左子树和右侧右子树 外圈
            stack.append(left.left)
            stack.append(right.right)

            # 内圈
            stack.append(left.right)
            stack.append(right.left)

        return True



# 层次遍历
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = collections.deque([root.left, root.right])

        while queue:
            level_size = len(queue)

            if level_size % 2 != 0:
                return False

            level_vals = []
            for i in range(level_size):
                node = queue.popleft()
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_vals.append(None)

            if level_vals != level_vals[::-1]:
                return False

        return True
