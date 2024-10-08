# Link to the exercise : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

############ INSTRUCTIONS ##############
########################################

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

############### EXERCISE ###############
########################################

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1

        while begin < end:
            midpoint = begin + (end - begin)//2

            if nums[midpoint] > nums[end]:
                begin = midpoint + 1
            
            else:
                end = midpoint
        return nums[begin]