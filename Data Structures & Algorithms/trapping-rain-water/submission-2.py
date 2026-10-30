class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        lmaxs = [0]*n
        rmaxs = [0]*n
        lmax=0
        for i in range(n):
            lmax = max(lmax, height[i])
            lmaxs[i] = lmax
        rmax=0
        for j in range(n-1,-1,-1):
            rmax = max(rmax, height[j])
            rmaxs[j] = rmax
        for k in range(n):
            ans+=min(lmaxs[k],rmaxs[k])-height[k]
        return ans