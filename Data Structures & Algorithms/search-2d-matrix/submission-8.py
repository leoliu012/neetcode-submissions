class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_items = []
        for row in matrix:
            first_items.append(row[0])
        l, r = 0, len(first_items)-1
        checks = [0] * len(first_items)
        while l <= r:
            m = (l+r)//2
            if first_items[m] < target:
                checks[m] = -1
                l = m+1
            elif first_items[m] > target:
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
        print(checks)
        print(to_search_ind)
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
        