class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seq = []
        for i in range(len(nums)):
            nums_seq.append([nums[i],i])
        nums_seq.sort()
        i, j = 0, len(nums)-1
        print(nums_seq)
        while i!=j:
            if nums_seq[i][0] + nums_seq[j][0] == target:
                return [min([nums_seq[i][1], nums_seq[j][1]]), max([nums_seq[i][1], nums_seq[j][1]])]
            elif nums_seq[i][0] + nums_seq[j][0] < target:
                i += 1
            else:
                j -= 1
        return [0,0]