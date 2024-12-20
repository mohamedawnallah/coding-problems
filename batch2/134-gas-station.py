class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        accumlative_gas, current_gas, starting_index = 0, 0, 0
        for i in range(len(gas)):
            accumlative_gas += gas[i]-cost[i]
            current_gas += gas[i]-cost[i]
            if current_gas < 0:
                current_gas = 0
                starting_index = i + 1
        if accumlative_gas < 0:
            return -1
        else:
            return starting_index % len(gas) 
