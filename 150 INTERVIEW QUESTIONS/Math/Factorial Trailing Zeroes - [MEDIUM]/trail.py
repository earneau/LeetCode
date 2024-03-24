# Link to the exercise : https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Given an integer n, return the number of trailing zeroes in n!.

#Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

############### EXERCISE ###############
########################################

def trailingZeroes(self, n):
    if n == 0:
        return 0

    i = n - 1

    while i >= 1:
        n = n * i
        i -= 1
    
    tmp = str(n)
    cpt = 0

    for letter in tmp:
        if letter == '0':
            cpt += 1
        else:
            cpt = 0
    
    return cpt