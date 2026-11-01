import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k):
            # print(k)
            sum = 0
            for pile in piles:
                sum+=math.ceil(pile/k)
            return sum<=h
        l=1
        r = max(piles)
        best = max(piles)
        while l<=r:
            # print(best)
            m = (r-l)//2+l
            if check(m):
                best = m
                r = m-1
            else:
                l = m+1
        return best

