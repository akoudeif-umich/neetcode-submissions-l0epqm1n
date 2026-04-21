# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        total = []
        
        for l in lists:
            node = l
            while node:
                total.append(node.val)
                node = node.next
        
        total.sort()

        if len(total) == 0:
            return None

        head = prev = ListNode(total[0])
        for i in range(1, len(total)):
            node = ListNode(total[i])
            prev.next = node
            prev = node


        return head
