class Solution:
    def jump(self, nums: List[int]) -> int:
        # furthest = 0
        # ret = 0
        if len(nums) <= 1:
            return 0
        # for i in range(len(nums)):
        #     if i + nums[i] > furthest:
        #         ret += 1
        #         furthest = i + nums[i]
        #         print(furthest)
        #     if furthest >= len(nums)-1:
        #         return ret
        # return ret
        i = 0
        ret = 0
        while i < len(nums):
            now_can_go = i+nums[i]
            furthest_dest = 0
            furthest_dest_ind = -1
            if now_can_go >= len(nums)-1:
                    return ret+1
            for j in range(i+1, now_can_go+1):
                if j >= len(nums):
                    return ret
                if j + nums[j] > furthest_dest:
                    furthest_dest_ind = j
                    furthest_dest = j + nums[j]
            i = furthest_dest_ind
            ret += 1
            
        return ret
