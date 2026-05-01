# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def merge(self, l1, l2):
        head = curr = ListNode()
        while l1 or l2:
            if l1 and not l2:
                curr.next = l1
                return head.next
            if l2 and not l1:
                curr.next = l2
                return head.next
            
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next
            
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.merge(lists[i - 1], lists[i])
        return lists[-1]
        


