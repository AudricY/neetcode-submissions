class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        max = 0
        for n in nums:

            if d[n] == 0:
                d[n] = d[n-1] + 1 + d[n+1]
                a = 1
                while d[n-a] != 0:
                    d[n-a] = d[n]
                    a += 1
                a = 1
                while d[n+a] != 0:
                    d[n+a] = d[n]
                    a += 1
                if d[n]> max: max=d[n]
        return max

# 1 2 3 4 5
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 2 2 0
# 1 0 2 2 0
# 4 4 4 4 0