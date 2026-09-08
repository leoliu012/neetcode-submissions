class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev_start, prev_end = intervals[0]
        ret = 0
        for (curr_start, curr_end) in intervals[1:]:
            if prev_end > curr_start:
                print(curr_start, curr_end)
                prev_end = min(curr_end, prev_end)
                ret += 1
            else:
                prev_end = curr_end
        return ret