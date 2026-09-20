class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # max_areas = []
        # for i in range(len(heights)):
        #     curr_bar = heights[i]
        #     max_height = curr_bar
        #     max_area = max_height
        #     for j in range(i+1, len(heights)):
        #         next_bar = heights[j]
        #         max_height = min(max_height, next_bar)
        #         max_area = max(max_height*(j-i+1), max_area)
        #     max_areas.append(max_area)

        # return max(max_areas)
        
        stack = []
        max_areas = []
        for i in range(len(heights)):
            old_bar_start = i
            while stack and stack[-1][0] > heights[i]:
                old_bar_height, old_bar_start = stack.pop()
                max_areas.append(old_bar_height * (i-old_bar_start))
            stack.append((heights[i], old_bar_start))
    

        while stack:
            old_bar_height, old_bar_start = stack.pop()
            max_areas.append(old_bar_height*(len(heights)  - old_bar_start))
            
        
        return max(max_areas)