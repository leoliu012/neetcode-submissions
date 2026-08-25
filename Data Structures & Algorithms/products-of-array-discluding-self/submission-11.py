class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_multi = 1
        num_0s = 0

        for i in range(len(nums)):
            all_multi *= nums[i] if nums[i] else 1
            if not nums[i]:
                num_0s += 1
        if num_0s>1:
            return [0] * len(nums)
        ret = []
        for each in nums:
            if num_0s and each != 0:
                ret.append(0)
            elif each == 0:
                ret.append(all_multi)
            else:
                ret.append(all_multi//each)
        return ret