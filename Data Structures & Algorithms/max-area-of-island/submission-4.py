class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(row, col):
            if (row, col) in visited or row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col]==0:
                return 0
            visited.add((row,col))

            return 1+dfs(row-1, col) +  dfs(row, col-1) +  dfs(row+1, col) + dfs(row, col+1)

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col]:
                    max_area = max(max_area, dfs(row, col))
        return max_area