class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            curr_ind = (r+l)//2
            if nums[curr_ind] < target:
                l = curr_ind+1
            elif nums[curr_ind] > target:
                r = curr_ind-1
            else:
                return curr_ind
        return -1