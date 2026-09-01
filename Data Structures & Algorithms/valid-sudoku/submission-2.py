class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_num = len(board)
        col_num = len(board[0])
        if (not row_num == 9) or (not col_num == 9):
            return False
        it = 0
        for row in range(row_num):
            row_set = set()
            for col in range(col_num):
                if not board[row][col] == '.':
                    curr = int(board[row][col])
                    if not curr >= 1 and curr <= 9:
                        return False
                    if curr in row_set:
                        return False
                    row_set.add(curr)
        
        for col in range(col_num):
            col_set = set()
            for row in range(row_num):
                if not board[row][col] == '.':
                    curr = int(board[row][col])
                    if curr in col_set:
                        return False
                    col_set.add(curr)
        
        for it_row in range(row_num//3):
            for it_col in range(row_num//3):
                square_set = set()
                for row in range(3):
                    for col in range(3):
                        if not board[row+it_row*3][col+it_col*3] == '.':
                            curr = int(board[row+it_row*3][col+it_col*3])
                            if curr in square_set:
                                return False
                            square_set.add(curr)
        return True