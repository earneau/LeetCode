# Link to the exercise : https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

############### EXERCISE ###############
########################################

# sliding window approach 

import sys

class Solution(object):

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0     # set up two pointers
        current_sum = 0
        min_length = sys.maxint     # set up to maximum int

        while j < len(nums):
            current_sum += nums[j]      # every iteration, add the current number
            while current_sum >= target:
                current_sum -= nums[i]      # if we go over the target number it means we've reached the target, so we remove the first number
                min_length = min(j-i+1,min_length)  # calculate if the current length of the sliding window is smaller than the min_length mesured
                i += 1  # move start pointer forward
            j += 1

        if min_length == sys.maxint:
            return 0     # if min_length is still as maximum int, then it means we havent found a subarray reaching target so we return 0

        return min_length