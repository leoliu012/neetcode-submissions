class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # visited = set()
        # def set_zero(row,col):
        #     for r in range(len(matrix)):
        #         matrix[r][col] = 0
        #     for c in range(len(matrix[0])):
        #         matrix[row][c] = 0
        # def divide(matrix_):
        #     for row in range(len(matrix_)):
        #         for col in range(len(matrix_[0])):
        #             if matrix_[row][col] == 0:
        #                 set_zero(row,col)
        #                 left_up = matrix_[:row]
        #                 for i in range(len(left_up)):
        #                     left_up[i] = left_up[i][:col]
        #                 right_up = matrix_[:row]
        #                 for i in range(len(right_up)):
        #                     right_up[i] = right_up[i][col+1:]

        #                 left_down = matrix_[row+1:]
        #                 for i in range(len(left_down)):
        #                     left_down[i] = left_down[i][:col]

        #                 right_down = matrix_[row+1:]
        #                 for i in range(len(right_down)):
        #                     right_down[i] = right_down[i][col+1:]
        #                 divide(left_up)
        #                 divide(right_up)
        #                 divide(left_down)
        #                 divide(right_down)
        #                 return
        
        # return divide(matrix)

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_zero = True

        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_zero = True

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0

        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0








        