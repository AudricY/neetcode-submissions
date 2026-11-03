# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(root, sub):
            if not root and not sub:
                return True
            if not root or not sub:
                return False
            if root.val != sub.val:
                return False
            return same(root.left, sub.left) and same(root.right,sub.right)
        
        
        def solve(root, sub):
            if not root:
                return False
            if solve(root.left, sub) or solve(root.right, sub) or same(root, sub): return True
            return False
        return solve(root, subRoot)
        