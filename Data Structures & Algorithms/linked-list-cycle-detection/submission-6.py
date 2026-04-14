# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        count = 0
        while head:
            if head in visited:
                return True
            visited[head] = count
            count += 1
            head = head.next
        return False