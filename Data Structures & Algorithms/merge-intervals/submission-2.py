# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         ret = []
        
#         for left,right in intervals:
#             inserted=0
#             for left_exist, right_exist in ret:
#                 if right_exist < left:
#                     ret.append([left_exist, right_exist])
#                 elif right < left_exist:
#                     if not inserted:
#                         ret.append([left, right])
#                     inserted = 1
#                 else:
#                     if not inserted:
#                         ret.append([min(left, left_exist), max(right, right_exist)])
#                     inserted = 1

#         return ret
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        for left, right in intervals:
            if not ret or ret[-1][1] < left:
                ret.append([left,right])
            else:
                ret[-1] = ([min(left, ret[-1][0]), max(right, ret[-1][1])])
        return ret