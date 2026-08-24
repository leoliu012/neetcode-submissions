class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs_ = {}
        for each in nums:
            freqs_[each] = 1 + freqs_.get(each, 0)
        freqs = []
        for key, val in freqs_.items():
            freqs.append([val, key])
        freqs.sort()
        freqs.reverse()
        ret = []
        for i in range(k):
            ret.append(freqs[i][1]) 
        return ret