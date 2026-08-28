import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def find_2_largest(nums):
            q = []
            rest = []
            for each in nums:
                heapq.heappush(q, each)
                if len(q) > 2:
                    rest.append(heapq.heappop(q))
            return q, rest
        while len(stones) > 1:
            [stone_a, stone_b],stones = find_2_largest(stones)
            left = abs(stone_a - stone_b)
            if left:
                stones.append(left)
        return stones[0] if stones else 0