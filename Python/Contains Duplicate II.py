# Link to the exercise : https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

############### EXERCISE ###############
########################################

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dictionary = {}

        for index, num in enumerate(nums):
            if num in dictionary:
                if abs(index - dictionary[num]) <= k:
                    return True
            
            dictionary[num] = index
        
        return False