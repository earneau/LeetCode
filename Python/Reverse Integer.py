# Link to the exercise : https://leetcode.com/problems/reverse-integer/description/

############ INSTRUCTIONS ##############
########################################

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

############### EXERCISE ###############
########################################

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maximum = pow(2,31) - 1
        minimum = - pow(2,31)

        sign = -1 if x < 0 else 1

        reverse = str(abs(x))[::-1]
        result = sign * int(reverse)

        if result >= minimum and result <= maximum:
            return result

        return 0        