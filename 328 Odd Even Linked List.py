# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        edummy = even = ListNode(None)
        odummy = odd = ListNode(None)
        while head:
            odd.next = head
            even.next = head.next
            even = even.next
            odd = odd.next
            head = head.next.next if even else None
        odd.next = edummy.next
        return odummy.next