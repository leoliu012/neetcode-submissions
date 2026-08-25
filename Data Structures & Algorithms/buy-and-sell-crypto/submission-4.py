class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        best = 0
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if buy < sell:
                best = max(best, sell-buy)
            else:
                l = r
            r += 1
        return best