class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mono_great_2 = [-1]*len(nums2)
        item_index = {}
        for j in range((len(nums2))):
            while stack and nums2[stack[-1]] < nums2[j]:
                num2_i = stack.pop()
                mono_great_2[num2_i] = j
            stack.append(j)
            item_index[nums2[j]] = j
        # print(mono_great_2)
        # print(item_index)
        ret = []
        for i in range((len(nums1))):
            num2_ind = item_index[nums1[i]]
            greater_ind = mono_great_2[num2_ind]
            if greater_ind != -1:
                ret.append(nums2[greater_ind])
            else:
                ret.append(greater_ind)
        return ret


