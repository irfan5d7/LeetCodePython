# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        while n:
            n-=1
            front = front.next
        if front == None:
            return head.next
        back = head
        while front and front.next:
            front = front.next
            back = back.next
        if back.next == None:
            return None
        back.next = back.next.next
        return head
            