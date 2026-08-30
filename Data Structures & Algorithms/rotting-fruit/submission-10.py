class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])
        first = True
        changed = False
        time = -1
        while changed or first:
            first = False
            changed = False
            for row in range(num_rows):
                for col in range(num_cols):
                    if grid[row][col] == 2:
                        if row+1 < num_rows and grid[row+1][col] == 1:
                            grid[row+1][col] = 3
                            changed = True
                        if row-1 >= 0 and grid[row-1][col] == 1:
                            grid[row-1][col] = 3
                            changed = True
                        if col+1 < num_cols and grid[row][col+1] ==1:
                            grid[row][col+1] = 3
                            changed = True
                        if col-1 >= 0 and grid[row][col-1] == 1:
                            grid[row][col-1] = 3 
                            changed = True
            for row in range(num_rows):
                for col in range(num_cols):
                    if grid[row][col] == 3:
                        grid[row][col] = 2
            time += 1
        for row in range(num_rows):
                for col in range(num_cols):
                    if grid[row][col] == 1:
                        return -1
        return time
            
        