class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = (x**2+y**2)**0.5
            if len(heap) >= k:
                (old_dist, (old_x,old_y)) = heapq.heappop(heap)
                old_dist = -old_dist
                if dist < old_dist:
                    heapq.heappush(heap, (-dist, (x, y))) 
                else:
                    heapq.heappush(heap, (-old_dist, (old_x,old_y))) 
            else:
                heapq.heappush(heap, (-dist, (x, y)))
        
        ret = []
        for each in heap:
            ret.append(each[1])
        return ret