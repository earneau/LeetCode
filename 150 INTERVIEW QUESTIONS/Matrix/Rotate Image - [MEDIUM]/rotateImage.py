############ INSTRUCTIONS ##############
########################################

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

############### EXERCISE ###############
########################################

def rotate(matrix):
    n = len(matrix)
    for i in range(n/2):
        for j in range(n-n/2):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                        matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]