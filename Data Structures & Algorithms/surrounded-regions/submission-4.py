class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        safe = set()
        visited = set()

        def dfs_safe(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in safe or board[row][col] == 'X':
                return
            if ((row, col) not in safe) and board[row][col] == 'O':
                safe.add((row,col))

            dfs_safe(row-1, col)
            dfs_safe(row+1, col)
            dfs_safe(row, col-1)
            dfs_safe(row, col+1)


        
        for row in range(rows):
            dfs_safe(row, 0)
            dfs_safe(row, cols-1)
        
        for col in range(cols):
            dfs_safe(0, col)
            dfs_safe(rows-1, col)
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in safe:
                    board[row][col] = 'X'