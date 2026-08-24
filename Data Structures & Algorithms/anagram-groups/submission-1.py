class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = {}
        for each in strs:
            key = [0]*26
            for s in each:
                key[ord(s)-ord('a')] += 1
            if tuple(key) not in ret:
                ret[tuple(key)] = []
            ret[tuple(key)].append(each)
        return list(ret.values())