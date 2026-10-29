class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        max = 0
        for n in nums:

            if d[n] == 0:
                left = d[n-1]
                right = d[n+1]
                length = left + 1 + right
                d[n] = length
                d[n-left] = length
                d[n+right] = length
                if d[n]> max: max=d[n]
        return max

# 1 2 3 4 5
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 2 2 0
# 1 0 2 2 0
# 4 4 4 4 0