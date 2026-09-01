class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordered = []
        for i in range(len(position)):
            ordered.append([position[i],speed[i]])
        ordered.sort()
        
        hours_takes = []
        for pos,s in ordered:
            remain = (target-pos)
            hours_takes.append(remain/s)
        
        ret = 1
        # in_fleet = False
        # for i in range(len(hours_takes)-1):
        #     if hours_takes[i] > hours_takes[i+1]:
        #         in_fleet = False
        #         ret += 1
        #     else:
        #         if not in_fleet:
        #             ret += 1
        # #             in_fleet = True
        res = set([hours_takes[-1]])
        if len(hours_takes) > 1:
            ind = len(hours_takes)-2
            while ind >= 0:
                if hours_takes[ind] > hours_takes[ind+1]:
                    # print(hours_takes[ind-1], hours_takes[ind])
                    res.add(hours_takes[ind])
                    ind -= 1
                else:
                    res.add(hours_takes[ind+1])
                    # print(ind-1, hours_takes[ind-1], hours_takes[ind])
                    slow = ind+1
                    while ind >= 0 and hours_takes[ind] <= hours_takes[slow]:
                        ind -= 1
        else:
            return 1

        return len(res)
            