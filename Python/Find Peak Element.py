# Link to the exercise : https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

############### EXERCISE ###############
########################################

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while begin < end:
            midpoint = begin + (end-begin)//2
            if (nums[midpoint] < nums[midpoint+1]):
                begin = midpoint + 1
            else:
                end = midpoint
        return begin
        