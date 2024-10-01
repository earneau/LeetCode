# Link to the exercise : https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

############ INSTRUCTIONS ##############
########################################

# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

############### EXERCISE ###############
########################################

class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factors = []

        for i in range(1,n+1):
            if (n % i == 0):
                factors.append(i)

        print(factors)
        if k <= len(factors):
            return factors[k-1]
        
        return -1