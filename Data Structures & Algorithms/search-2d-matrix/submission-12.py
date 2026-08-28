class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        checks = [0] * len(matrix)
        while l <= r:
            m = (l+r)//2
            if matrix[m][0] < target:
                checks[m] = -1
                l = m+1
            elif matrix[m][0]  > target:
                checks[m] = 1
                r = m-1
            else:
                return True
        to_search_ind = 0
        for i in range(len(checks)-1):
            if checks[i] == -1 and checks[i+1] == 1:
                to_search_ind = i
            elif checks[i+1] == -1:
                to_search_ind = i+1
        to_search = matrix[to_search_ind]
        l, r = 0, len(to_search)-1
        while l <= r:
            m = (l+r)//2
            if to_search[m] < target:
                l = m+1
            elif to_search[m] > target:
                r = m-1
            else:
                return True
        return False
        