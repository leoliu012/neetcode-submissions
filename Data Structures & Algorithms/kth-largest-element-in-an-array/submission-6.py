import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for each in nums:
            heapq.heappush(q, -each)
        ret = -1
        for i in range(k):
            ret = heapq.heappop(q)
        return -ret
