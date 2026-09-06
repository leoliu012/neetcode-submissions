class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for i, t in enumerate(tasks):
            counts[t] = 1 + counts.get(t, 0)
        
        heap = []
        for key, val in counts.items():
            heap.append([-val, key])
        
        heapq.heapify(heap)
        cooling = []

        cycles = 0
        while heap or cooling:
            if cooling:
                next_task_cycle, next_remaining, next_task = cooling[0]
                if cycles == next_task_cycle:
                    heapq.heappop(cooling)
                    heapq.heappush(heap,[-next_remaining, next_task])

            if heap:
                remaining, curr_task =heapq.heappop(heap)
                remaining = -remaining
                if remaining-1 > 0:
                    heapq.heappush(cooling,[cycles+n+1, remaining-1, curr_task])

            cycles += 1
        return cycles