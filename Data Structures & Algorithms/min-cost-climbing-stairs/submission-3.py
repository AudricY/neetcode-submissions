class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1]*n
        cache[0], cache[1] = cost[0], cost[1]
        for i in range(2, n):
            cache[i] = min(cache[i-1], cache[i-2]) + cost[i]
        return min(cache[n-1], cache[n-2])