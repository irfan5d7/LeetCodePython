# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def rec(node):
            if not node: return None
            rec(node.right)
            rec(node.left)
            
            node.right = self.prev
            node.left = None
            self.prev = node
            return self.prev
        k = rec(node = root)
        return k
                