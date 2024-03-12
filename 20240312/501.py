# leetcode 501 二叉搜索树中的众数

# 第一种 常规遍历二叉树的递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        maps = {}
        self.searchBST(root, maps)

        max_freq = max(maps.values())
        for key, value in maps.items():
            if value == max_freq:
                result.append(key)

        return result

    def searchBST(self, node, maps):
        if not node:
            return

        maps[node.val] = maps.get(node.val, 0) + 1

        self.searchBST(node.left, maps)
        self.searchBST(node.right, maps)



# 第二种 写了个迭代法来试一下


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return None
        # 用迭代法去写

        cur = root
        pre = None

        stack = []
        maxCount = 0
        count = 0
        res = []

        while cur is not None or len(stack) > 0:
            if cur:
                stack.append(cur)
                cur = cur.left

            else:
                cur = stack.pop()
                if not pre:
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else:
                    count = 1

                if count == maxCount:
                    res.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    res = []
                    res.append(cur.val)

                pre = cur
                cur = cur.right

        return res





