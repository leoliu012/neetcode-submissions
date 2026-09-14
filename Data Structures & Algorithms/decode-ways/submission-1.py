class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(len(s)):
            for j in range(i+1,min(len(s)+1,i+3)):
                candidate = s[i:j]
                if dp[i] and (str(int(candidate)) == candidate
                                        and int(candidate) <= 26 and int(candidate) >= 1):
                    dp[j] += dp[i]
        return dp[-1]
                    
