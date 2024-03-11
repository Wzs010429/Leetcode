# leetcode 105 从前序和中序遍历序列构造二叉树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        middle_root = preorder[0]

        root = TreeNode(middle_root)
        root_index = inorder.index(middle_root)

        inorderLeftTree = inorder[:root_index]
        inorderRightTree = inorder[root_index+1:]

        preLeftTree = preorder[1:len(inorderLeftTree)+1]
        preRightTree = preorder[len(inorderLeftTree)+1:]

        root.left = self.buildTree(preLeftTree, inorderLeftTree)
        root.right = self.buildTree(preRightTree, inorderRightTree)

        return root
