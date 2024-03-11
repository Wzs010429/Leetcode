# leetcode 106 从中序和后序遍历序列构造二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        split_val = postorder[-1]

        # 这个就是根节点
        root = TreeNode(split_val)
        split_index = inorder.index(split_val)

        # 分离中序
        leftTree = inorder[:split_index]
        rightTree = inorder[split_index + 1:]

        # 分离后序
        postLeftTree = postorder[:len(leftTree)]
        postRightTree = postorder[len(leftTree):-1]

        root.left = self.buildTree(leftTree, postLeftTree)
        root.right = self.buildTree(rightTree, postRightTree)

        return root
