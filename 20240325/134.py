# leetcode 134 加油站

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        curSum = 0
        totalSum = 0

        startIndex = 0

        for i in range(len(gas)):
            curSum += gas[i] - cost[i]

            totalSum += gas[i] - cost[i]

            if curSum < 0:
                startIndex = i+1
                curSum = 0
            
        if totalSum < 0:
            return -1
        return startIndex