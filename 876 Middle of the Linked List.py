# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit = head
        turtle = head
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            turtle = turtle.next
        return turtle