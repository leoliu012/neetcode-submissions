class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getArea(ind1, ind2, h1, h2):
            return abs(ind2-ind1) * (min(h1,h2))
        curr_area = 0
        max_area = 0
        l, r = 0, len(heights)-1
        while l<r:
            curr_area = getArea(l,r,heights[l],heights[r])
            if curr_area > max_area:
                max_area = curr_area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
