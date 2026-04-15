# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.max_diff = 0

        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left < right:
                self.max_diff = max(self.max_diff, right - left)
            else:
                self.max_diff = max(self.max_diff, left - right)

            return 1 + max(left, right)
        
        dfs(root)

        if self.max_diff > 1:
            return False
        return True

        