class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        le = len(heights)
        l = 0
        r = le-1
        best = 0
        while l != r:
            curr = min(heights[l],heights[r]) * (r-l)
            best = max(curr,best)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return best
            