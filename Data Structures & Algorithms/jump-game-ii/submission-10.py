class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        ret = 0
        curr_loc = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            
            if i == curr_loc:
                curr_loc = farthest
                ret += 1
        return ret