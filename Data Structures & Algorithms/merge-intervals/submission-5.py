class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        i = 0
        while i < len(intervals)-1:
            l1, l2 = intervals[i][0], intervals[i+1][0]
            r1, r2 = intervals[i][1], intervals[i+1][1]
            overlap = r1>=l2
            if overlap:
                l = l1
                r = max(r1,r2)
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [l,r])
            else:
                i+=1
        return intervals
        