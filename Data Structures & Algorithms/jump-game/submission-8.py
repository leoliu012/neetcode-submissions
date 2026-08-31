# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         def jump(curr_ind, nums, target):
#             if curr_ind >= target:
#                 return curr_ind
#             now_available = nums[curr_ind]
#             furthest = 0
#             for i in range(1, now_available+1):
#                 furthest = max(jump(curr_ind+i, nums, target), furthest)
#             return furthest if furthest else curr_ind
#         target = len(nums)-1
#         furthest_ind = jump(0, nums, target)
#         if furthest_ind >= target:
#             return True
#         return False
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for i in range(len(nums)):
            if furthest >= i:
                furthest = max(furthest, i + nums[i])
            else:
                return False
        return True
