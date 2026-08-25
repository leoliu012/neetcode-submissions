class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = set()
        for i in range(len(nums)):
            compl = 0 - nums[i]

            l,r = i+1, len(nums)-1
            
            while l<r:
                tmp = nums[l] + nums[r]
                if tmp < compl:
                    l+=1
                elif tmp > compl:
                    r-=1
                else:
                    ret.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
        return list(ret)