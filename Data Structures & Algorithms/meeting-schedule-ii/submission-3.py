"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:

#         def overlaps(s,r, rs,re):
#             return s < re
#         def nonoverlap_dist(s,e, rs,re):
#             return s - re

#         intervals.sort(key=lambda item: item.start)

#         rooms = []
#         for each in intervals:
#             start, end = each.start, each.end
#             min_overlap = float('inf')
#             room_i = -1
#             for i in range(len(rooms)):
#                 r_start, r_end = rooms[i]
#                 overlap_time = start - r_end
#                 if not overlaps(start, end, r_start, r_end) and overlap_time < min_overlap:
#                     min_overlap = overlap_time
#                     room_i = i
#             if room_i != -1:
#                 rooms[room_i] = (min(start, rooms[room_i][0]), max(end, rooms[room_i][1]))
#             else:
#                 rooms.append((start, end))
        

#         return len(rooms)
                
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        heapq.heapify(rooms)
        intervals.sort(key=lambda item: item.start)
        for each in intervals:
            start, end = each.start, each.end
            if not rooms:
                heapq.heappush(rooms, end)
            else:
                earliest_r_end = heapq.heappop(rooms)
                if start >= earliest_r_end:
                    heapq.heappush(rooms, end)
                else:
                    heapq.heappush(rooms, end)
                    heapq.heappush(rooms, earliest_r_end)

        return len(rooms)