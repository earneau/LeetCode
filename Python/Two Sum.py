# Link to the exercise : https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

############### EXERCISE ###############
########################################

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        second = 0

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    first = i
                    second = j
        
        return [first,second]