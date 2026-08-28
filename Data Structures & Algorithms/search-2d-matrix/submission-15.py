class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l+r)//2
            if matrix[m][0] < target:
                l = m+1
            elif matrix[m][0]  > target:
                r = m-1
            else:
                return True
        to_search_ind = r

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
        