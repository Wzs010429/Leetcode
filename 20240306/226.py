# leetcode 226 反转二叉树


# 第一种 递归法 前序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



# 第二种 迭代法 前序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]

        while stack:
            tmp = stack.pop()
            tmp.left, tmp.right = tmp.right, tmp.left
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)

        return root


# 递归法 中序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.invertTree(root.left)
        root.left, root.right = root.right, root.left

        # 这里注意两次都是反转左边 因为上面左右交换了
        self.invertTree(root.left)

        return root







