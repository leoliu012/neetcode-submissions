class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ret = []
        def dfs(candidates, nums, start):
            if sum(candidates) == target:
                ret.append(candidates.copy())
                return
            if sum(candidates) < target:
                for i in range(start, len(nums)):
                    candidates.append(nums[i])
                    dfs(candidates, nums, i)
                    candidates.pop()
                
        dfs([], nums, 0)

        return ret