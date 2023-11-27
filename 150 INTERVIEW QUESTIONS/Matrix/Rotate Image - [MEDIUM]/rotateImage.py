############ INSTRUCTIONS ##############
########################################

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

############### EXERCISE ###############
########################################

import numpy as np

def rotate(matrix):
    n = len(matrix[0])
    matrix = np.array(matrix)

    for i in range(0,n):
        top = matrix[i][i:n-i]
        bottom = matrix[n-i-1][i:n-i]
        left = matrix[:,i][i:n-i]
        right = matrix[:,n-i-1][i:n-i]

        print("top: ",top)
        print("bottom: ",bottom)
        print("left: ",left[::-1])
        print("right: ",right[::-1])
        matrix[:,n-i-1][i:n-i] = top
        matrix[n-i-1][i:n-i] = right[::-1]
        matrix[:,i][i:n-i] = bottom
        matrix[i][i:n-i] = left[::-1]
        print(matrix)
        print("\n")