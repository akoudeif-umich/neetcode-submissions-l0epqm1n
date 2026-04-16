# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def heightOfNode(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.heightOfNode(root.left), self.heightOfNode(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.heightOfNode(root.left)
        right = self.heightOfNode(root.right)

        return max(left + right, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))