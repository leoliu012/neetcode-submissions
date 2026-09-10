class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        temp = []
        def dfs(length, start):
            if len(temp) == length:
                ret.append(temp.copy())
                return
            i = start
            while i  < len(nums):
                temp.append(nums[i])
                dfs(length, i+1)
                temp.pop()
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                    i +=1
                i += 1

        nums.sort()
        for length in range(len(nums) + 1):
            dfs(length, 0)
        return ret