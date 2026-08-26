# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         def check_equal(s1:str, s2:str) -> bool:
#             if len(s1)!=len(s2):
#                 return False
#             s1_count = {}
#             s2_count = {}
#             for each in s1:
#                 s1_count[each] = 1 + s1_count.get(each, 0)
#             for each in s2:
#                 s2_count[each] = 1 + s2_count.get(each, 0)
#             return s1_count == s2_count
#         contains = set(list(s1))

#         for i in range(len(s2) - len(s1)+1):
#             if s2[i] in contains:
#                 if check_equal(s1, s2[i:i+len(s1)]):
#                     return True
#         return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def count(s1:str) -> list[str]:
            s1_count = [0]*26
            for each in s1:
                s1_count[ord(each)-ord('a')] += 1
            return s1_count
        s1_count = count(s1)

        l = 0
        s2_sub = [0]*26
        for r in range(len(s2)):
            
            s2_sub[ord(s2[r])-ord('a')] += 1
            
            if r-l+1 > len(s1):
                s2_sub[ord(s2[l])-ord('a')] -= 1
                l += 1
            print(s2_sub)
            if s2_sub == s1_count:
                return True

            
        return False