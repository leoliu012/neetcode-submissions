# import heapq
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         def find_2_largest(nums):
#             q = []
#             rest = []
#             for each in nums:
#                 heapq.heappush(q, each)
#                 if len(q) > 2:
#                     rest.append(heapq.heappop(q))
#             return q, rest
#         while len(stones) > 1:
#             [stone_a, stone_b],stones = find_2_largest(stones)
#             left = abs(stone_a - stone_b)
#             if left:
#                 stones.append(left)
#         return stones[0] if stones else 0

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for each in stones:
            q.append(-each)
        heapq.heapify(q)
        while len(q) > 1:
            stone_a, stone_b = -(heapq.heappop(q)), -(heapq.heappop(q))
            left = abs(stone_a - stone_b)
            if left:
                heapq.heappush(q, -left)
        return -q[0] if q else 0


