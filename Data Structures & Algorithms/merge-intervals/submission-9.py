class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_end = ans[-1][1]
            cur_start, cur_end = intervals[i][0], intervals[i][1]
            if prev_end>=cur_start: #overlap
                ans[-1][1] = max(cur_end, prev_end)
            else:
                ans.append([cur_start, cur_end])
        return ans
        