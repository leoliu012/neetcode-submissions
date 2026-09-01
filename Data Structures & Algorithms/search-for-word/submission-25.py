class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(row,col, board, word):
            
            num_row = len(board)
            num_col = len(board[0])
            if word == '':
                return True
            visited.add((row, col))
            # print(visited)
            if row > 0:
                if board[row-1][col] == word[0] and (row-1, col) not in visited:
                    # print(board[row-1][col])
                    # visited.add((row-1, col))
                    if dfs(row-1, col, board, word[1:]):
                        return True
                    # visited.remove((row-1, col))
            if row < num_row-1:
                if board[row+1][col] == word[0] and (row+1, col) not in visited:
                    # print(board[row+1][col])
                    # visited.add((row+1, col))
                    if dfs(row+1, col, board, word[1:]):
                        return True
                    # visited.remove((row+1, col))
            if col > 0:
                if board[row][col-1] == word[0] and (row, col-1) not in visited:
                    # print(board[row][col-1], row, col-1)
                    # visited.add((row, col-1))
                    if dfs(row, col-1, board, word[1:]):
                        return True
                    # visited.remove((row, col-1))
            if col < num_col-1:
                if board[row][col+1] == word[0] and (row, col+1) not in visited:
                    # print( board[row][col+1], row, col+1, word)
                    if dfs(row, col+1, board, word[1:]):
                        return True
            # print(1, visited)
            visited.remove((row, col))
            return False

        start = word[0]
        num_row = len(board)
        num_col = len(board[0])
        
        for row in range(num_row):
            for col in range(num_col):
                if board[row][col] == start:
                    print(row,col)
                    visited = set()
                    if dfs(row,col, board, word[1:]):
                        return True
        return False