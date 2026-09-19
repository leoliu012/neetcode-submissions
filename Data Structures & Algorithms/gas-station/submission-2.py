class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # for i in range(len(gas)):
        #     curr_gas = 0
        #     for j in range(len(gas)):
        #         curr_index = (i+j)%len(gas)
        #         curr_gas += gas[curr_index]
        #         curr_gas -= cost[curr_index]
        #         if curr_gas < 0:
        #             break
        #     if curr_gas >= 0:
        #         return i
        # return -1
            
        net_gain = [0] * len(gas)
        max_i = 0
        max_gain = 0
        for i in range(len(gas)):
            net_gain[i] = gas[i] - cost[i]
        #     if net_gain[i] > max_gain:
        #         max_gain = net_gain[i]
        #         max_i = i
        # print(net_gain)
        if sum(net_gain) < 0:
            return -1

        curr_gas = 0
        ret = 0
        for i in range(len(gas)):
            curr_gas += net_gain[i]
            if curr_gas < 0:
                ret = i+1
                curr_gas = 0
        return ret