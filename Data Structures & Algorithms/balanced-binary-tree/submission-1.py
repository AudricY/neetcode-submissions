# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if not node: return True, 0
            balanced_l, height_l = solve(node.left)
            balanced_r, height_r = solve(node.right)

            balanced = abs(height_l-height_r)<=1 and balanced_l and balanced_r
            height = max(height_l,height_r)+1
            return balanced, height
        return solve(root)[0]
        