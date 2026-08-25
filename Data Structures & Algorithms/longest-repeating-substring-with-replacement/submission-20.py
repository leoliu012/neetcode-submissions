class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        ret = 0
        counts = {}
        max_count = 0

        if len(s) < 1:
            return 0

        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_count = max(counts[s[r]], max_count)
            
            if (r-l+1 - max_count) > k:
                counts[s[l]] -= 1
                l += 1

            ret = max(ret, r-l+1)
            r += 1
        return ret