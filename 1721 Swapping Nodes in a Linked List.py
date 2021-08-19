# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node1, node2, curr = None, None, head
        while curr:
            k-=1
            node2 = None if node2 == None else node2.next
            if k == 0:
                node1 = curr
                node2 = head
            curr = curr.next
        val = node1.val
        node1.val = node2.val
        node2.val = val
        return head
        