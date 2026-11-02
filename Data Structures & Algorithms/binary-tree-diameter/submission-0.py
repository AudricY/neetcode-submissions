# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def solve(node):
            if not node: return 0, 0
            max_depth_l, diameter_l = solve(node.left)
            max_depth_r, diameter_r = solve(node.right)
            max_depth = 1+ max(max_depth_l,max_depth_r)
            diameter = max((max_depth_l+max_depth_r), max(diameter_l,diameter_r))
            return max_depth, diameter
        ans = solve(root)
        print(ans)
        return ans[1]

        