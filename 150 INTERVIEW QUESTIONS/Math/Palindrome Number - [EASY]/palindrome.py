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