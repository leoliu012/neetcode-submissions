class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        temp = []
        def dfs(i):
            if sum(temp) > target:
                return
            if sum(temp) == target:
                ret.append(temp.copy())
            for each in nums[i:]:
                temp.append(each)
                dfs(i)
                i += 1
                temp.pop()
        dfs(0)
        return ret    