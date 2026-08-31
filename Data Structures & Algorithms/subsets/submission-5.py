class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(i, subset):
            if i == len(nums):
                ret.append(subset.copy())
                return
            dfs(i+1, subset)
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
        dfs(0, [])
        return ret