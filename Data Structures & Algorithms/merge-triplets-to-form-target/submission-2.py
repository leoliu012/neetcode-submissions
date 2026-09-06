class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # for i in range(len(triplets)):
        #     triplet_i = triplets[i]
        #     for j in range(i, len(triplets)):
        #         triplet_j = triplets[j]
        #         new_triplet_j = [max(triplet_i[0],triplet_j[0]), max(triplet_i[1],triplet_j[1]), max(triplet_i[2],triplet_j[2])]
        #         if new_triplet_j == target:
        #             return True
        # return False

        ret = [-1, -1 ,-1]
        for each in triplets:
            if each[0] == target[0] and each[1] <= target[1] and each[2] <= target[2]:
                ret[0] = each[0]
            if each[1] == target[1] and each[0] <= target[0] and each[2] <= target[2]:
                ret[1] = each[1]
            if each[2] == target[2] and each[0] <= target[0] and each[1] <= target[1]:
                ret[2] = each[2]
            if ret == target:
                return True
        return False