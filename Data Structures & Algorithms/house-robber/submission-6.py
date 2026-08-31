class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(nums)>1:
            dp[1] = nums[1]
            for i in range(2,len(nums)):
                max_money = 0
                for j in range(i-1):
                    max_money = max(max_money, max(dp[i-1], (dp[j]+nums[i])))
                dp[i] = max_money
        return max(dp)