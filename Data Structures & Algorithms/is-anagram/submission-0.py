class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set()
        s_dict = dict()

        t_set = set()
        t_dict = dict()
        for each in s:
            if each not in s_set:
                s_dict[each] = 1
                s_set.add(each)
            else:
               s_dict[each] += 1
            
        for each in t:
            if each not in t_set:
                t_dict[each] = 1
                t_set.add(each)
            else:
               t_dict[each] += 1
        
        if s_set != t_set:
            return False
        
        for each in s_dict:
            s_nums = s_dict[each]
            t_nums = t_dict[each]
            if s_nums != t_nums:
                return False
        return True
