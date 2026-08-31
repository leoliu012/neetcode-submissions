class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_count = {0:1}
        ret = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            rest = prefix - k
            if rest in pre_count:
                ret += pre_count[rest]
            pre_count[prefix] = 1 + pre_count.get(prefix, 0)
        return ret

