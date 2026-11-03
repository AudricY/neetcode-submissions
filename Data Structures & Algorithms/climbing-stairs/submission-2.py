class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0,1,2] + [-1]*(n-2)
        for i in range(3, n+1):
            res[i] = res[i-1]+res[i-2]
        print(res)
        return res[n]