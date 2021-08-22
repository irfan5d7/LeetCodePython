"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head : return None
        dummy = Node(None,None,head,None)
        curr = dummy
        prev = None
        stack = [head]
        while stack:
            node = stack.pop()
            curr.next = node
            node.prev = curr
            
            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
            curr = node
        dummy.next.prev = None
        return dummy.next
            