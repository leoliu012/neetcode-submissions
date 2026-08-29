class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_cols = len(grid[0])
        num_rows = len(grid)
        rets = 0
        def dfs(x,y):
            if x<0 or x>= num_cols or y< 0 or y>= num_rows:
                return
            if grid[y][x] == '1':
                grid[y][x] = '0'
            else:
                return
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    rets += 1
                    dfs(col, row)
        return rets