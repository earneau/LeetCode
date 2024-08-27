# Link to the exercise : https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Given an integer x, return true if x is a palindrome, and false otherwise.

############### EXERCISE ###############
########################################

def isPalindrome(x):
    order = str(x)
    disorder = order[::-1]
    if disorder == order:
        return True
    else:
        return False