class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        for i in range(1,amount+1):
            denom_options = []
            for denom in coins:
                if i-denom >= 0 and dp[i-denom] != -1:
                    denom_options.append((dp[i-denom]))
            dp[i] = min(denom_options)+1 if denom_options else -1
        return dp[amount]
                

            
            