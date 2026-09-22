class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)
        def can_ship(cap):
            i = 0
            day_used = 0
            while i < len(weights):
                curr_weight = 0
                while i < len(weights) and weights[i] + curr_weight <= cap:
                    curr_weight += weights[i]
                    i += 1
                day_used += 1
            
            return day_used
        candidates = [x for x in range(min_cap, max_cap+1)]

        l,r = 0, len(candidates)-1
        while l < r:
            m = (l+r)//2

            if can_ship(candidates[m]) <= days:
                r = m
            elif can_ship(candidates[m]) > days:
                l = m+1
        return candidates[l]
            

                