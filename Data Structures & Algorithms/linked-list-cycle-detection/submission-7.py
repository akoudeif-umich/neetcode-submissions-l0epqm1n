# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tracker = {} # node : index
        index = 0

        while head:
            if head in tracker:
                return True

            tracker[head] = index
            index += 1
            head = head.next

        return False
