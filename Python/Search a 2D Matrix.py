# Link to the exercise : https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

############### EXERCISE ###############
########################################

class Solution(object):
    def flatten(self, matrix):
        result = []
        for sublist in matrix:
            for item in sublist:
                result.append(item)
        return result

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        flat = self.flatten(matrix)

        begin = 0
        end = len(flat) - 1

        while begin <= end:
            midpoint = begin + (end-begin)//2
            midpoint_value = flat[midpoint]

            if midpoint_value == target:
                return True
            elif target < midpoint_value:
                end = midpoint-1
            else:
                begin = midpoint+1
        
        return False