class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return max(nums)
        nums_no_rob0 = nums[1:]
        dp_no_rob0 = [0] * len(nums_no_rob0)
        dp_no_rob0[0] = nums_no_rob0[0]
        if len(nums_no_rob0) > 1:
            dp_no_rob0[1] = max(nums_no_rob0[0], nums_no_rob0[1])
            for i in range(2, len(nums_no_rob0)):
                dp_no_rob0[i] = max(dp_no_rob0[i-1], dp_no_rob0[i-2]+nums_no_rob0[i])


        nums_no_robl = nums[:-1]
        dp_no_robl = [0] * len(nums_no_robl)
        dp_no_robl[0] = nums_no_robl[0]
        if len(nums_no_robl) > 1:
            dp_no_robl[1] = max(nums_no_robl[0], nums_no_robl[1])
            for i in range(2, len(nums_no_robl)):
                dp_no_robl[i] = max(dp_no_robl[i-1], dp_no_robl[i-2]+nums_no_robl[i])


        return max(max(dp_no_rob0), max(dp_no_robl))
        