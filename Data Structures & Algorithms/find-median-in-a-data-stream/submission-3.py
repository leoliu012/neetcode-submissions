class MedianFinder:

    def __init__(self):
        self.large_min_heap = []
        self.small_max_heap = []
        self.medians = []

    def addNum(self, num: int) -> None:
        
        if not self.small_max_heap:
            heapq.heappush(self.small_max_heap, -num)
            return
        

        small_max_val = -self.small_max_heap[0] #smaller part

        # print(small_max_val)
        if small_max_val >= num:
            heapq.heappush(self.small_max_heap, -num)
        else:
            heapq.heappush(self.large_min_heap, num)
        
        if abs(len(self.large_min_heap)-len(self.small_max_heap)) > 1:
            if len(self.large_min_heap)>len(self.small_max_heap):
                new_val = heapq.heappop(self.large_min_heap)
                heapq.heappush(self.small_max_heap, -new_val)
            else:
                new_val = -heapq.heappop(self.small_max_heap)
                heapq.heappush(self.large_min_heap, new_val)

        # print(self.small_max_heap, self.large_min_heap)

        

    def findMedian(self) -> float:
        total_num = len(self.large_min_heap) + len(self.small_max_heap)
        if total_num %2 ==0:
            # print(888, self.small_max_heap, self.large_min_heap)
            return (self.large_min_heap[0] + -self.small_max_heap[0])/2
        else:
            if len(self.large_min_heap)>len(self.small_max_heap):
                return self.large_min_heap[0]
            else:
                return -self.small_max_heap[0]
        
        
        