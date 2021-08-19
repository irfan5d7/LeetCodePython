# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        curr = head
        while curr.next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev
        head.next = None
        return curr
            
            
        