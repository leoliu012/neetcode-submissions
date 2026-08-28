class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_rotation_num(nums:int) -> int:
            l, r = 0, len(nums)-1
            while l < r:
                m = (l+r)//2
                if nums[m]>nums[r]:
                    l = m+1
                else:
                    r = m
            return l


        def convert_m_to_rotated(rotation_times:int, lr:int) -> int:
            return (rotation_times+lr)%len(nums)

        rotation_times =  get_rotation_num(nums)

        orig_l, orig_r = 0, len(nums)-1
        while orig_l <= orig_r:
            m = orig_l+(orig_r-orig_l)//2
            converted_m = convert_m_to_rotated(rotation_times,m)
            if nums[converted_m] < target:
                orig_l = m+1
            elif nums[converted_m] > target:
                orig_r = m-1
            else:
                return converted_m
        return -1
