# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         all_multi = 1
#         num_0s = 0

#         for i in range(len(nums)):
#             all_multi *= nums[i] if nums[i] else 1
#             if not nums[i]:
#                 num_0s += 1
#         if num_0s>1:
#             return [0] * len(nums)
#         ret = []
#         for each in nums:
#             if num_0s and each != 0:
#                 ret.append(0)
#             elif each == 0:
#                 ret.append(all_multi)
#             else:
#                 ret.append(all_multi//each)
#         return ret
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n

        pre[0] = 1
        suf[n-1] = 1
        ret = []
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(n):
            ret.append(pre[i] * suf[i])
        return ret