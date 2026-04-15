# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        best = 0
        while stack:
            node = stack.pop()
            if node:
                best = max(best, 
                        self.maxDepth(node.left) +  
                        self.maxDepth(node.right)
                )
                stack.append(node.left)
                stack.append(node.right)
        return best


