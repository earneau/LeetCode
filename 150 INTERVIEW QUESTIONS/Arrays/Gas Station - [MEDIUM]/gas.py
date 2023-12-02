############ INSTRUCTIONS ##############
########################################

#There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

#Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
#If there exists a solution, it is guaranteed to be unique

############### EXERCISE ###############
########################################

def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    tank = 0
    l = len(gas)

    if sum(gas) < sum(cost):
        return -1 
        
    for start in range(0,l):
        if gas[start] < cost[start]:
            continue

        tank += gas[start]
        i = l - 1
        tip = start
        
        
        while i >= 0:
            tank -= cost[tip]
            if tank >= 0:
                tip += 1
                if tip >= l:
                    tip = 0
                tank += gas[tip]
            else:
                tank = 0
                break
            i -= 1
        
        if tip == start:
            return start

    return -1

