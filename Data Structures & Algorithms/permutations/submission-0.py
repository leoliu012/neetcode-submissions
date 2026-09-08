class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        temp = []
        def dfs(nums):
            if not nums:
                print(temp)
                ret.append(temp.copy())
                return
            for i in range(len(nums)):
                temp.append(nums[i])
                dfs(nums[:i] + nums[i+1:])
                temp.pop()
        dfs(nums)
        
        return ret