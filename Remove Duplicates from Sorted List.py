# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        while t and t.next:
            if t.val == t.next.val:
                t.next = t.next.next
            else:
                t = t.next
        return head
        