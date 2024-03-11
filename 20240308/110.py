# leetcode 110 平衡二叉树

## 第一种 递归法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 用递归法去做的
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1

    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if left == -1 or right == -1 or (abs(left - right) > 1):
            return -1
        else:
            return max(right, left) + 1



# 第二种 迭代法

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ## 自己手写一下迭代法

        if not root:
            return True

        stack = [root]
        heightDict = {}

        while stack:
            tmp = stack.pop()
            if tmp:
                stack.append(tmp)
                stack.append(None)
                if tmp.left: stack.append(tmp.left)
                if tmp.right: stack.append(tmp.right)
            else:
                realNode = stack.pop()
                leftHeight, rightHeight = heightDict.get(realNode.left, 0), heightDict.get(realNode.right, 0)
                if abs(leftHeight - rightHeight) > 1:
                    return False

                else:
                    heightDict[realNode] = max(leftHeight, rightHeight) + 1

        return True

# 这个还蛮有意思的 可以好好思考一下