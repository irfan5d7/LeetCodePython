# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                break
        if fast == None or fast.next == None:
            return None
        res = head
        while res != slow:
            res = res.next
            slow = slow.next
        return slow
        
        