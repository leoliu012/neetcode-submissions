class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_take(k, piles, h):
            if k == 0:
                return -1
            total_h = 0
            for i in range(len(piles)):
                if piles[i]%k == 0:
                    total_h += piles[i]//k
                else:
                    total_h += piles[i]//k+1
            return total_h

        l, r = 0, max(piles)
        ret = 1
        while l <= r:
            m = (l+r)//2
            if m < 1:
                return ret
            total_h = time_take(m, piles, h)
            if total_h <= h:
                ret = m
                r = m-1
            else:
                l = m+1
        return ret
