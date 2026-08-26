class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check_equal(s1:str, s2:str) -> bool:
            if len(s1)!=len(s2):
                return False
            s1_count = {}
            s2_count = {}
            for each in s1:
                s1_count[each] = 1 + s1_count.get(each, 0)
            for each in s2:
                s2_count[each] = 1 + s2_count.get(each, 0)
            return s1_count == s2_count
        contains = set(list(s1))

        for i in range(len(s2) - len(s1)+1):
            if s2[i] in contains:
                if check_equal(s1, s2[i:i+len(s1)]):
                    return True
        return False