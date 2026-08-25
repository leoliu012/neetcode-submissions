class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1 if nums else 0
        curr_longest = 1 if nums else 0
        nums = set(nums)

        for each in nums:
            if each-1 not in nums: # start
                while curr_longest+each in nums:
                    curr_longest += 1
                if curr_longest > longest:
                    longest = curr_longest
                curr_longest = 1
        return longest



            