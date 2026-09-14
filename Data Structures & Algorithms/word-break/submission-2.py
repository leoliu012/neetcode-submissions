class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)

        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                frame = s[i:j]
                if dp[i]:
                    # print(frame)
                    dp[j] = dp[j] or (frame in wordDict)
                elif i == 0:
                    print(j)
                    print(frame, frame in wordDict)
                    dp[j] = (frame in wordDict)
                    print(dp[j])
        print(dp)
        return dp[-1]
