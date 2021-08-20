# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        dummy = ListNode(None,head)
        lnode = dummy
        for i in range(left):
            prev = lnode
            lnode = lnode.next
        rnode = lnode
        for i in range(right-left):
            rnode = rnode.next
        rdum = ListNode(None,lnode)
        rprev = rdum
        while lnode!= rnode:
            nxt = lnode.next
            lnode.next= rprev
            rprev = lnode
            lnode = nxt
        nxt = lnode.next
        lnode.next = rprev
        rdum.next.next = nxt
        rdum.next = None
        prev.next = lnode
        return dummy.next