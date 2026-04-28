# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def size(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        
        return count
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        head = None

        if self.size(l1) > self.size(l2):
            head = curr = l1
            other = l2
        else:
            head = curr = l2
            other = l1


        while curr:
            if carry:
                curr.val += 1
                carry = False
            
            if other:
                curr.val += other.val

            if curr.val >= 10:
                curr.val -= 10
                carry = True
            
            if not curr.next and carry:
                node = ListNode(1)
                curr.next = node
                break

            curr = curr.next
            
            if other:
                other = other.next

        return head
            