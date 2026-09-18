class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(row, col):
            if grid[row][col] and (row, col) not in visited:
                visited.add((row,col))
                if row - 1 >= 0:
                    dfs(row-1, col)
                if col - 1 >= 0:
                    dfs(row, col-1)
                if row+1 < len(grid):
                    dfs(row+1, col)
                if col+1 < len(grid[0]):
                    dfs(row, col+1)
            else:
                return

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col]:
                    before_visited = len(visited)
                    dfs(row, col)
                    max_area = max(max_area, len(visited)-before_visited)
        return max_area