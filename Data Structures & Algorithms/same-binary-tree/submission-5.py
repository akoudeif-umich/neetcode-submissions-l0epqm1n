# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque([(p, q)])

        while dq:
            node1, node2 = dq.popleft()
            
            if node1 and node2 and node1.val == node2.val:
                dq.append((node1.left, node2.left))
                dq.append((node1.right, node2.right))
            elif not node1 and not node2:
                continue
            else:
                return False
        return True