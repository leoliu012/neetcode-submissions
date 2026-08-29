class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        ret = []
        new_created = 0
        inserted = 0
        for left, right in intervals:
            if left > newInterval[1]:
                if not inserted:
                    ret.append(newInterval)
                    inserted = 1
                ret.append([left,right])
            elif right < newInterval[0]:
                ret.append([left,right])
            else:
                newInterval = [min(newInterval[0], left), max(newInterval[1], right)]
        if not inserted:
            ret.append(newInterval)
        return ret