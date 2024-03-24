# Link to the exercise : https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

#You must do it in place.

############### EXERCISE ###############
########################################

def setZeroes(matrix):
    n = len(matrix[0]) #row
    m = len(matrix[:])  #col

    # matrix[i][j] <= 2**31 - 1 so we set rows of 0s to a higher value
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 0:
                for row in range (0,n):
                    if matrix[i][row] != 0:
                        matrix[i][row] = 2**31
                for col in range (0,m):
                    if matrix[col][j] != 0:
                        matrix[col][j] = 2**31

    # we replace marked numbers by the high value with 0s
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 2**31:
                matrix[i][j] = 0