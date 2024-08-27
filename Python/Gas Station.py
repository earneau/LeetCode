# Link to the exercise : https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

#Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
#If there exists a solution, it is guaranteed to be unique

############### EXERCISE ###############
########################################

def canCompleteCircuit(self, gas, cost):
    l = len(gas)
    
    ptrR = l - 1
    ptrL = 0
    tank = 0
    while ptrL <= ptrR:
        if tank < 0:
            tank += gas[ptrR] - cost[ptrR]
            ptrR -= 1
        else:
            tank += gas[ptrL] - cost[ptrL]
            ptrL += 1
    return ptrL % l if tank >= 0 else -1