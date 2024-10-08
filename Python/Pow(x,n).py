# Link to the exercise : https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

############### EXERCISE ###############
########################################

class Solution(object):
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n/2)