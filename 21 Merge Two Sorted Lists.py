# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        t = dummy
        t1 = l1
        t2 = l2
        while t1 and t2:
            if t1.val <= t2.val:
                t.next = t1
                t1=t1.next
            else:
                t.next = t2
                t2=t2.next
            t = t.next
        t.next = t1 or t2
        return dummy.next